import { Console } from "console";

export function makePerson(name: string, age: number) {
  return { name: name, age: age };
}

export function testMakePerson() {
  console.log(makePerson("Jane", 12), makePerson("Jake", 16));
}
