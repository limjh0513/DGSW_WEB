import { createRangeIterable } from "./createRangeIterable";

const iterator = createRangeIterable(1, 3 + 1);
while (true) {
  const { value, done } = iterator.next();
  if (done) break;
  //@ts-ignore
  console.log(value);
}
