// Language: typescript
// Path: react-next\utils\predict.ts
import { getImageTensorFromPath } from './imageHelper';
import { runModel } from './modelHelper';

type Prediction = {
  efficientnet: [any, number],
  resnet18: [any, number],
  resnet50: [any, number],
  mobilenetS: [any, number],
  mobilenetL: [any, number],
  alexnet: [any, number]
};

export async function inference(path: string): Promise<Prediction> {
  // 1. Convert image to tensor
  const imageTensor = await getImageTensorFromPath(path);
  // 2. Run each model model
  // 3. Return predictions and the amount of time it took to inference.
  return {
    efficientnet:  await runModel(imageTensor, 'efficientnet-b4-40'),
    resnet18: await runModel(imageTensor, 'resnet18-20'),
    resnet50: await runModel(imageTensor, 'resnet50-95'),
    mobilenetS: await runModel(imageTensor, 'mobilenetv3-s-20'),
    mobilenetL: await runModel(imageTensor, 'mobilenetv3-20'),
    alexnet: [0, 0]
  }
}

