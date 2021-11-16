import { makePerson } from "./person/Person";
import IPerson from "./person/IPerson";

const testMakePerson = (): void => {
  let Jane: IPerson = makePerson("Jane");
  let Jake: IPerson = makePerson("Jake");
  console.log(Jane, Jake);
};

testMakePerson();
