# JavaScript - Objects, Scopes and Closures

Alright, people, let's get our legs in the water!

## Classes

Classes are a template for creating objects. They encapsulate data with code to work on that data. Classes in JS are built on prototypes but also have some syntax and semantics that are unique to classes.

### Defining classes

Classes are in fact "special functions", and just as you can define **function expressions**(when you ```variable = function(parameters){code}```) and **function declarations**, a class can be defined in two ways: a **class expression** or a **class declaration**.

```javascript
// Declaration
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}

// Expression; the class is anonymous but assigned to a variable
const Rectangle = class {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};

// Expression; the class has its own name
const Rectangle = class Rectangle2 {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};

```

Like function expressions, class expressions may be **anonymous**, or have a name that's different from the variable that it's assigned to. However, unlike function declarations, class declarations have the same temporal dead zone restrictions as ```let``` or ```const``` and behave as if they are not hoisted. Meaning it's genrally going to be A WHOLE LOT easier when you write variables that have been declared with ```let```, ```const```, and ```class``` at the top of the block/scope they're being used in. so:

```javascript
function example() {
  let x;
  console.log(x); // undefined
  x = 10;
  // ...
}
```

is better and easier to deal with than:

```javascript
function example() {
  console.log(x); // ReferenceError: Cannot access 'x' before initialization
  let x = 10;
  // ...
}
```

### Class body

The body of a class is the part that is in curly braces ```{}```. This is where you define class members, such as methods or constructor.

A class element can be characterized by three aspects:

* Kind: Getter, setter, method, or field
* Location: Static or instance
* Visibility: Public or private

In addition, there are two special class element syntaxes: ```constructor``` and static initialization blocks, with their own references.

### Constructor

The ```constructor``` method is a special method for creating and initializing an object created with a class. There can only be one special method with the name "constructor" in a class — a ```SyntaxError``` is thrown if the class contains more than one occurrence of a ```constructor``` method.

A constructor can use the ```super``` keyword to call the constructor of the super class.

You can create instance properties inside the constructor:

```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}

```

Alternatively, if your instance properties' values do not depend on the constructor's arguments, you can define them as **class fields.**

### Static initialization blocks

Static initialization blocks allow flexible initialization of static properties, including the evaluation of statements during initialization, while granting access to the private scope.

Multiple static blocks can be declared, and these can be interleaved with the declaration of static fields and methods (all static items are evaluated in declaration order).

### Methods

Methods are defined on the prototype of each class instance and are shared by all instances. Methods can be plain functions, async functions, generator functions, or async generator functions.

```javascript

class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  // Getter
  get area() {
    return this.calcArea();
  }
  // Method
  calcArea() {
    return this.height * this.width;
  }
  *getSides() {
    yield this.height;
    yield this.width;
    yield this.height;
    yield this.width;
  }
}

const square = new Rectangle(10, 10);

console.log(square.area); // 100
console.log([...square.getSides()]); // [10, 10, 10, 10]
```

### Static methods and fields

The ```static``` keyword defines a static method or field for a class. Static properties (fields and methods) are defined on the class itself instead of each instance. Static methods are often used to create utility functions for an application, whereas static fields are useful for caches, fixed-configuration, or any other data that doesn't need to be replicated across instances.

```javascript
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  static displayName = "Point";
  static distance(a, b) {
    const dx = a.x - b.x;
    const dy = a.y - b.y;

    return Math.hypot(dx, dy);
  }
}

const p1 = new Point(5, 5);
const p2 = new Point(10, 10);
p1.displayName; // undefined
p1.distance; // undefined
p2.displayName; // undefined
p2.distance; // undefined

console.log(Point.displayName); // "Point"
console.log(Point.distance(p1, p2)); // 7.0710678118654755

```

### Field declarations

With the class field declaration syntax, the constructor example can be written as:

```javascript
class Rectangle {
  height = 0;
  width;
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}

```

Class fields are similar to object properties, not variables, so we don't use keywords such as ```const``` to declare them. In JavaScript, private features use a special identifier syntax, so modifier keywords like ```public``` and ```private``` should not be used either.

As seen above, the fields can be declared with or without a default value. Fields without default values default to ```undefined```. By declaring fields up-front, class definitions become more self-documenting, and the fields are always present, which help with optimizations.

### Private properties

Using private fields, the definition can be refined as below.

```javascript
class Rectangle {
  #height = 0;
  #width;
  constructor(height, width) {
    this.#height = height;
    this.#width = width;
  }
}

```

It's an error to reference private fields from outside of the class; they can only be read or written within the class body. By defining things that are not visible outside of the class, you ensure that your classes' users can't depend on internals, which may change from version to version.

Private fields can only be declared up-front in a field declaration. They cannot be created later through assigning to them, the way that normal properties can.

### Inheritance

The ```extends``` keyword is used in class declarations or class expressions to create a class as a child of another constructor (either a class or a function).

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a noise.`);
  }
}

class Dog extends Animal {
  constructor(name) {
    super(name); // call the super class constructor and pass in the name parameter
  }

  speak() {
    console.log(`${this.name} barks.`);
  }
}

const d = new Dog("Mitzie");
d.speak(); // Mitzie barks.

```

If there is a constructor present in the subclass, it needs to first call ```super()``` before using ```this```. The ```super``` keyword can also be used to call corresponding methods of super class.

```javascript
class Cat {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a noise.`);
  }
}

class Lion extends Cat {
  speak() {
    super.speak();
    console.log(`${this.name} roars.`);
  }
}

const l = new Lion("Fuzzy");
l.speak();
// Fuzzy makes a noise.
// Fuzzy roars.

```

### Binding this with instance and static methods

When a static or instance method is called without a value for ```this```, such as by assigning the method to a variable and then calling it, the ```this``` value will be ```undefined``` inside the method.

```javascript
class Animal {
  speak() {
    return this;
  }
  static eat() {
    return this;
  }
}

const obj = new Animal();
obj.speak(); // the Animal object
const speak = obj.speak;
speak(); // undefined

Animal.eat(); // class Animal
const eat = Animal.eat;
eat(); // undefined

```

## super

The ```super``` keyword is used to access properties on an object literal or class's [[Prototype]], or invoke a superclass's constructor.

```javascript
super([arguments]) // calls the parent constructor.
super.propertyOnParent
super[expression]
```

The ```super``` keyword can be used in two ways: as a "function call" (```super(...args)```), or as a "property lookup" (```super.prop``` and ```super[expr]```).

**Note:** ```super``` is a keyword and these are special syntactic constructs. ```super``` is not a variable that points to the prototype object. Attempting to read ```super``` itself is a ```SyntaxError```.

In the constructor body of a derived class (with ```extends```), the ```super``` keyword may appear as a "function call" (```super(...args)```), which must be called before the ```this``` keyword is used, and before the constructor returns. It calls the parent class's constructor and binds the parent class's public fields, after which the derived class's constructor can further access and modify ```this```.

Note that the reference of ```super``` is determined by the class or object literal super was declared in, not the object the method is called on. Therefore, unbinding or re-binding a method doesn't change the reference of ```super``` in it (although they do change the reference of ```this```). You can see ```super``` as a variable in the class or object literal scope, which the methods create a closure over. (But also beware that it's not actually a variable, as explained above.)

When setting properties through ```super```, the property is set on ```this``` instead.

### Using super in classes

Here ```super()``` is called to avoid duplicating the constructor parts' that are common between ```Rectangle``` and ```Square```.

```javascript
class Rectangle {
  constructor(height, width) {
    this.name = "Rectangle";
    this.height = height;
    this.width = width;
  }
  sayName() {
    console.log(`Hi, I am a ${this.name}.`);
  }
  get area() {
    return this.height * this.width;
  }
  set area(value) {
    this._area = value;
  }
}

class Square extends Rectangle {
  constructor(length) {
    // Here, it calls the parent class's constructor with lengths
    // provided for the Rectangle's width and height
    super(length, length);

    // Note: In derived classes, super() must be called before you
    // can use 'this'. Moving this to the top causes a ReferenceError.
    this.name = "Square";
  }
}

```

### Super-calling static methods

You are also able to call super on static methods.

```javascript
class Rectangle {
  static logNbSides() {
    return "I have 4 sides";
  }
}

class Square extends Rectangle {
  static logDescription() {
    return `${super.logNbSides()} which are all equal`;
  }
}
Square.logDescription(); // 'I have 4 sides which are all equal'

```

### Accessing super in class field declaration

```super``` can also be accessed during class field initialization. The reference of ```super``` depends on whether the current field is an instance field or a static field.

```javascript
class Base {
  static baseStaticField = 90;
  baseMethod() {
    return 10;
  }
}

class Extended extends Base {
  extendedField = super.baseMethod(); // 10
  static extendedStaticField = super.baseStaticField; // 90
}

```

Note that instance fields are set on the instance instead of the constructor's ```prototype```, so you can't use ```super``` to access the instance field of a superclass. so the code below is very wrong:

```javascript
class Base {
  baseField = 10;
}

class Extended extends Base {
  extendedField = super.baseField; // undefined
}

```

Here, ```extendedField``` is ```undefined``` instead of ```10```, because ```baseField``` is defined as an own property of the ```Base``` instance, instead of ```Base.prototype```. ```super```, in this context, only looks up properties on ```Base.prototype```, because that's the ```[[Prototype]]``` of ```Extended.prototype```.

### Deleting super properties will throw an error

You cannot use the ```delete``` operator and ```super.prop``` or ```super[expr]``` to delete a parent class' property — it will throw a ```ReferenceError```.

```javascript
class Base {
  foo() {}
}
class Derived extends Base {
  delete() {
    delete super.foo; // this is bad
  }
}

new Derived().delete(); // ReferenceError: invalid delete involving 'super'.

```

### Using super.prop in object literals

Super can also be used in the object initializer notation. In this example, two objects define a method. In the second object, ```super``` calls the first object's method. This works with the help of ```Object.setPrototypeOf()``` with which we are able to set the prototype of ```obj2``` to ```obj1```, so that ```super``` is able to find method1 on ```obj1```.

```javascript
const obj1 = {
  method1() {
    console.log("method 1");
  },
};

const obj2 = {
  method2() {
    super.method1();
  },
};

Object.setPrototypeOf(obj2, obj1);
obj2.method2(); // Logs "method 1"

```

### Calling methods from super

When calling ```super.prop``` as a function, the ```this``` value inside the prop function is the current ```this```, not the object that ```super``` points to. For example, the ```super.getName()``` call logs "Extended", despite the code looking like it's equivalent to ```Base.getName().```

```javascript
class Base {
  static getName() {
    console.log(this.name);
  }
}

class Extended extends Base {
  static getName() {
    super.getName();
  }
}

Extended.getName(); // Logs "Extended"

```

This is especially important when interacting with static private properties.

### Setting ```super.prop``` sets the property on ```this``` instead

This is one of the cases where understanding ```super``` as simply "reference of the prototype object" falls short, because it actually sets the property on ```this``` instead.

```javascript
class A {}
class B extends A {
  setX() {
    super.x = 1;
  }
}

const b = new B();
b.setX();
console.log(b); // B { x: 1 }
console.log(Object.hasOwn(b, "x")); // true

```

```super.x = 1``` will look for the property descriptor of ```x``` on ```A.prototype``` (and invoke the setters defined there), but the ```this``` value will be set to ```this```, which is ```b``` in this context.

This means that while methods that **get** ```super.prop``` are usually not susceptible to changes in the this context, those that **set** ```super.prop``` are.

```javascript
/* Reusing same declarations as above */

const b2 = new B();
b2.setX.call(null); // TypeError: Cannot assign to read only property 'x' of object 'null'
```

However, ```super.x = 1``` still consults the property descriptor of the prototype object, which means you cannot rewrite non-writable properties, and setters will be invoked.

```javascript
class X {
  constructor() {
    // Create a non-writable property
    Object.defineProperty(this, "prop", {
      configurable: true,
      writable: false,
      value: 1,
    });
  }
}

class Y extends X {
  constructor() {
    super();
  }
  foo() {
    super.prop = 2; // Cannot overwrite the value.
  }
}

const y = new Y();
y.foo(); // TypeError: "prop" is read-only
console.log(y.prop); // 1

```

## extends

The ```extends``` keyword is used in class declarations or class expressions to create a class that is a child of another class.

The ```extends``` keyword can be used to subclass custom classes as well as built-in objects.

Any constructor that can be called with ```new``` and has the ```prototype``` property can be the candidate for the parent class. The two conditions must both hold — for example, bound functions and Proxy can be constructed, but they don't have a ```prototype``` property, so they cannot be subclassed.

```javascript
function OldStyleClass() {
  this.someProperty = 1;
}
OldStyleClass.prototype.someMethod = function () {};

class ChildClass extends OldStyleClass {}

class ModernClass {
  someProperty = 1;
  someMethod() {}
}

class AnotherChildClass extends ModernClass {}

```

The ```prototype``` property of the ```ParentClass``` must be an ```Object``` or ```null```, but you would rarely worry about this in practice, because a non-object prototype doesn't behave as it should anyway. (It's ignored by the ```new``` operator.)

```javascript
function ParentClass() {}
ParentClass.prototype = 3;

class ChildClass extends ParentClass {}
// Uncaught TypeError: Class extends value does not have valid prototype property 3

console.log(Object.getPrototypeOf(new ParentClass()));
// [Object: null prototype] {}
// Not actually a number!

```

```extends``` sets the prototype for both ```ChildClass``` and ```ChildClass.prototype```.

<table speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
  <thead speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <th speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"></th>
      <th speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Prototype of <code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">ChildClass</code></th>
      <th speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Prototype of <code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">ChildClass.prototype</code></th>
    </tr>
  </thead>
  <tbody speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">extends</code> clause absent</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">Function.prototype</code></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">Object.prototype</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="#extending_null" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">extends null</code></a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">Function.prototype</code></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">null</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">extends ParentClass</code></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">ParentClass</code></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">ParentClass.prototype</code></td>
    </tr>
  </tbody>
</table>

```javascript
class ParentClass {}
class ChildClass extends ParentClass {}

// Allows inheritance of static properties
Object.getPrototypeOf(ChildClass) === ParentClass;
// Allows inheritance of instance properties
Object.getPrototypeOf(ChildClass.prototype) === ParentClass.prototype;

```

The right-hand side of ```extends``` does not have to be an identifier. You can use any expression that evaluates to a constructor. This is often useful to create mixins. The ```this``` value in the ```extends``` expression is the ```this``` surrounding the class definition, and referring to the class's name is a ```ReferenceError``` because the class is not initialized yet. ```await``` and ```yield``` work as expected in this expression.

```javascript
class SomeClass extends class {
  constructor() {
    console.log("Base class");
  }
} {
  constructor() {
    super();
    console.log("Derived class");
  }
}

new SomeClass();
// Base class
// Derived class

```

While the base class may return anything from its constructor, the derived class **must return an object or ```undefined```, or a ```TypeError``` will be thrown**.

```javascript
class ParentClass {
  constructor() {
    return 1;
  }
}

console.log(new ParentClass()); // ParentClass {}
// The return value is ignored because it's not an object
// This is consistent with function constructors

class ChildClass extends ParentClass {
  constructor() {
    super();
    return 1;
  }
}

console.log(new ChildClass()); // TypeError: Derived constructors may only return object or undefined

```

If the parent class constructor returns an object, that object will be used as the ```this``` value for the derived class when further initializing class fields. This trick is called "return overriding", which allows a derived class's fields (including private ones) to be defined on unrelated objects.

## Closure

Let's say it's... related to **lexical scoping**.

And this particularly means that if we have a function B with no variables in function A. Function B prints variable C that actually exists in Function A. Function B will find that Variable C is not in it, so what does it do? It's gonna look for it in its nearest predecessor, which is Function A. It's gonna find it there so its gonna print variable C as per what it was in function A.

**Note:** Use ```const``` and you have a global variable no matter where you put it. use ```let``` or ```const``` and you'll have a block-scoped variable.

## Binding

It's a big thing honestly so here's [this link](https://alistapart.com/article/getoutbindingsituations/) for it.
