"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.testMakePerson = exports.makePerson = void 0;
function makePerson(name, age) {
    return { name: name, age: age };
}
exports.makePerson = makePerson;
function testMakePerson() {
    console.log(makePerson("Jane", 12), makePerson("Jake", 16));
}
exports.testMakePerson = testMakePerson;
//# sourceMappingURL=makePerson.js.map