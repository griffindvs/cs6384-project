// Language: typescript
// Path: react-next\utils\predict.ts
import { getImageTensorFromPath } from './imageHelper';
import { runModel } from './modelHelper';

type Prediction = {
  resnet: [any, number],
  mobilenet: [any, number],
  alexnet: [any, number]
};

export async function inference(path: string): Promise<Prediction> {
  // 1. Convert image to tensor
  const imageTensor = await getImageTensorFromPath(path);
  // 2. Run each model model
  const [rPred, rTime] = await runModel(imageTensor, 'resnet18-20');
  const [mPred, mTime] = await runModel(imageTensor, 'mobilenetv3-s-20');
  // const [aPred, aTime] = await runModel(imageTensor, 'resnet18-20');
  // 3. Return predictions and the amount of time it took to inference.
  return {
    resnet: [rPred, rTime],
    mobilenet: [mPred, mTime],
    alexnet: [0, 0]
  }
}

