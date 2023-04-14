import { useRef, useState } from 'react';
import { Button, Input } from 'reactstrap';
import { inference } from '../utils/predict';
import styles from '../styles/Home.module.css';

interface Props {
  height: number;
  width: number;
}

const ImageCanvas = (props: Props) => {

  const canvasRef = useRef<HTMLCanvasElement>(null);
  var image: HTMLImageElement;
  const [topResultLabel, setLabel] = useState("");
  const [topResultConfidence, setConfidence] = useState("");
  const [inferenceTime, setInferenceTime] = useState("");
  
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
    setLabel(`Inferencing...`);
    setConfidence("");
    setInferenceTime("");

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
    var [inferenceResult,inferenceTime] = await inference(image.src);

    // Get the highest confidence.
    var topResult = inferenceResult[0];

    // Update the label and confidence
    setLabel(topResult.name.toUpperCase());
    setConfidence(topResult.probability);
    setInferenceTime(`Inference speed: ${inferenceTime} seconds`);

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
      <span>{topResultLabel} {topResultConfidence}</span>
      <span>{inferenceTime}</span>
    </>
  )

};

export default ImageCanvas;
