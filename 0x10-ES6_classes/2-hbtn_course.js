export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('name must be a String');
    if (typeof length !== 'number') throw TypeError('length must be a Number');
    if (students.constructor !== Array && students.every((el) => typeof el === 'string')) {
      throw TypeError('students must be an Array of Strings');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(theName) {
    if (typeof theName !== 'string') throw TypeError('name must be a String');
    this._name = theName;
  }

  get name() {
    return this._name;
  }

  set length(theLength) {
    if (typeof theLength !== 'number') throw TypeError('length must be a Number');
    this._length = theLength;
  }

  get length() {
    return this._length;
  }

  set students(theStudents) {
    if (theStudents.constructor !== Array && theStudents.every((el) => typeof el === 'string')) {
      throw TypeError('students must be an Array of Strings');
    }
    this._students = theStudents;
  }

  get students() {
    return this._students;
  }
}
