import { useRef, useState } from 'react';
import { Button, Input, Row, Col } from 'reactstrap';
import { inference } from '../utils/predict';
import styles from '../styles/Home.module.css';

interface Props {
  height: number;
  width: number;
}

const ImageCanvas = (props: Props) => {

  const canvasRef = useRef<HTMLCanvasElement>(null);
  var image: HTMLImageElement;
  const [waiting, setWaiting] = useState("");

  const [rLabel, setRLabel] = useState("");
  const [rConfidence, setRConfidence] = useState("");
  const [rTime, setRTime] = useState("");

  const [mLabel, setMLabel] = useState("");
  const [mConfidence, setMConfidence] = useState("");
  const [mTime, setMTime] = useState("");

  const [aLabel, setALabel] = useState("");
  const [aConfidence, setAConfidence] = useState("");
  const [aTime, setATime] = useState("");
  
  // Load the image from the IMAGE_URLS array
  const getImage = (e: React.ChangeEvent<HTMLInputElement>) => {
    let file = (e.target as HTMLInputElement).files![0]
    displayImageAndRunInference(file);
  }

  // Draw image and other  UI elements then run inference
  const displayImageAndRunInference = (file: File) => { 
    // Get the image
    image = new Image();

    try {
      image.src = URL.createObjectURL(file);
    } catch (error) {
      console.log(error);
    }

    // Clear out previous values.
    setWaiting(`Inferencing...`);
    setRLabel("");
    setRConfidence("");
    setRTime("");
    setMLabel("");
    setMConfidence("");
    setMTime("");
    setALabel("");
    setAConfidence("");
    setATime("");

    // Draw the image on the canvas
    const canvas = canvasRef.current;
    const ctx = canvas!.getContext('2d');
    image.onload = () => {
      ctx!.drawImage(image, 0, 0, props.width, props.height);
    }
   
    // Run the inference
    submitInference();
  };

  const submitInference = async () => {

    // Get the image data from the canvas and submit inference.
    var resultsObj = await inference(image.src);
    setWaiting("");

    // Res-Net
    if (resultsObj['resnet'][0] > 0.5) {
      setRLabel("Healthy");
    } else {
      setRLabel("Diseased");
    }
    setRConfidence(resultsObj['resnet'][0].toFixed(5));
    setRTime(`Inference speed: ${resultsObj['resnet'][1]}s`);

    // MobileNet
    if (resultsObj['resnet'][0] > 0.5) {
      setMLabel("Healthy");
    } else {
      setMLabel("Diseased");
    }
    setMConfidence(resultsObj['mobilenet'][0].toFixed(5));
    setMTime(`Inference speed: ${resultsObj['mobilenet'][1]}s`);

    // AlexNet
    if (resultsObj['alexnet'][0] > 0.5) {
      setALabel("Healthy");
    } else {
      setALabel("Diseased");
    }
    setAConfidence(resultsObj['alexnet'][0].toFixed(5));
    setATime(`Inference speed: ${resultsObj['alexnet'][1]}s`);
    
  };

  return (
    <>
      <Input 
        type="file"
        accept="image/*" 
        id="file-input" 
        onChange={getImage}
        className="m-4"
      />
      {/* <Button
        color="primary"
        className={styles.grid}
        onClick={displayImageAndRunInference} >
        Run detection
      </Button> */}
      <br/>
      <canvas ref={canvasRef} width={props.width} height={props.height} />
      <Row>
        {waiting && <span>{waiting}</span>}
        <Col className={styles.colBox}>
          {rLabel && <h4>Res-Net 18:</h4>}
          {rLabel && <span>{rLabel} | Confidence: {rConfidence}</span>}
          <span className={styles.block}>{rTime}</span>
        </Col>
        <Col className={styles.colBox}>
          {mLabel && <h4>MobileNetV3:</h4>}
          {mLabel && <span>{mLabel} | Confidence: {mConfidence}</span>}
          <span className={styles.block}>{mTime}</span>
        </Col>
        <Col className={styles.colBox}>
          {aLabel && <h4>AlexNet:</h4>}
          {aLabel && <span>{aLabel} | Confidence: {aConfidence}</span>}
          <span className={styles.block}>{aTime}</span>
        </Col>
      </Row>
    </>
  )

};

export default ImageCanvas;
