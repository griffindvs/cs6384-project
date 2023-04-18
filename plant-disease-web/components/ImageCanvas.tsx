import { useRef, useState } from 'react';
import { Button, Input, Row, Col } from 'reactstrap';
import { inference } from '../utils/predict';
import styles from '../styles/Home.module.css';

interface Props {
  height: number;
  width: number;
}

type Prediction = {
  efficientnet: [any, number],
  resnet18: [any, number],
  resnet50: [any, number],
  mobilenetS: [any, number],
  mobilenetL: [any, number],
  alexnet: [any, number]
};

const initialPrediction = {
  efficientnet: [0, 0],
  resnet18: [0, 0],
  resnet50: [0, 0],
  mobilenetS: [0, 0],
  mobilenetL: [0, 0],
  alexnet: [0, 0]
}

const ImageCanvas = (props: Props) => {

  const canvasRef = useRef<HTMLCanvasElement>(null);
  var image: HTMLImageElement;
  const [waiting, setWaiting] = useState("");

  const [results, setResults] = useState(initialPrediction);
  
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
    setResults(resultsObj);
    setWaiting("");
    
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
      {waiting && <span>{waiting}</span>}
      {results['mobilenetS'][0] !== 0 && 
      <Row>
        <Col className={styles.colBox}>
          <h4>MobileNetV3 (Small):</h4>
          <span className={styles.block}>6.1 MB</span>
          <span>{results['mobilenetS'][0] > 0.5 ? "Healthy" : "Diseased"} | Confidence: {(Math.abs(results['mobilenetS'][0]-0.5)*2.0).toFixed(5)}</span>
          <span className={styles.block}>Time: {results['mobilenetS'][1]}s</span>
        </Col>
        <Col className={styles.colBox}>
          <h4>MobileNetV3 (Large):</h4>
          <span className={styles.block}>16.8 MB</span>
          <span>{results['mobilenetL'][0] > 0.5 ? "Healthy" : "Diseased"} | Confidence: {(Math.abs(results['mobilenetL'][0]-0.5)*2.0).toFixed(5)}</span>
          <span className={styles.block}>Time: {results['mobilenetL'][1]}s</span>
        </Col>
        <Col className={styles.colBox}>
          <h4>EfficientNet-B4:</h4>
          <span className={styles.block}>70.1 MB</span>
          <span>{results['efficientnet'][0] > 0.5 ? "Healthy" : "Diseased"} | Confidence: {(Math.abs(results['efficientnet'][0]-0.5)*2.0).toFixed(5)}</span>
          <span className={styles.block}>Time: {results['efficientnet'][1]}s</span>
        </Col>
      </Row> }
      {results['mobilenetS'][0] !== 0 && 
      <Row>
        <Col className={styles.colBox}>
          <h4>Res-Net 18:</h4>
          <span className={styles.block}>44.7 MB</span>
          <span>{results['resnet18'][0] > 0.5 ? "Healthy" : "Diseased"} | Confidence: {(Math.abs(results['resnet18'][0]-.5)*2.0).toFixed(5)}</span>
          <span className={styles.block}>Time: {results['resnet18'][1]}s</span>
        </Col>
        <Col className={styles.colBox}>
          <h4>Res-Net 50:</h4>
          <span className={styles.block}>94 MB</span>
          <span>{results['resnet50'][0] > 0.5 ? "Healthy" : "Diseased"} | Confidence: {(Math.abs(results['resnet50'][0]-.5)*2.0).toFixed(5)}</span>
          <span className={styles.block}>Time: {results['resnet50'][1]}s</span>
        </Col>
        <Col className={styles.colBox}>
          <h4>AlexNet:</h4>
          <span className={styles.block}>228 MB</span>
          <span className={styles.block}><em>Model file too large for GitHub Pages.</em></span>
          {/* {aLabel && <span>{aLabel} | Confidence: {aConfidence}</span>}
          <span className={styles.block}>{aTime}</span> */}
        </Col>
      </Row> }
    </>
  )

};

export default ImageCanvas;
