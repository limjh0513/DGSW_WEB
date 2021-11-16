//import { makeRandomNumber } from "../util/makeRandomNumber";
import * as U from "../util/makeRandomNumber";
import IPerson from "../person/IPerson";

export class Person implements IPerson {
  constructor(public name: string, public age: number) {}
}

export const makePerson = (
  name: string,
  age: number = U.makeRandomNumber()
) => ({
  name,
  age,
});
