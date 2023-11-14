# Javascript

**Ahhh Javascript. Trust me, it's a terrifying language. Even Python gets scared of it sometimes...**

![JSmeme](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/303/Javascript-535.png.jpeg)

## Okay let's get straight to it cuz it's still cool

And by cool I mean it adds interactivity to your website. This happens in games, in the behavior of responses when buttons are pressed or with data entry on forms; with dynamic styling; with animation, etc. Developers have written a variety of tools on top of the core JavaScript language, unlocking a vast amount of functionality with minimum effort. These include:

* Browser Application Programming Interfaces (APIs) built into web browsers, providing functionality such as dynamically creating HTML and setting CSS styles; collecting and manipulating a video stream from a user's webcam, or generating 3D graphics and audio samples.
* Third-party APIs that allow developers to incorporate functionality in sites from other content providers, such as Twitter or Facebook.
* Third-party frameworks and libraries that you can apply to HTML to accelerate the work of building sites and applications.

### Mmm... Where exactly do I write and put my javascript code?

As for the writing you can literally write it anywhere you want (even inside your HTML itself in the ```<script>``` tag) as long as the file is **.js** extension(if you're doing it externally) and you're not actuallly writing it on a paper.

Now as for where to put it, in your HTML document, of course(my Egyptian fellows reading this will have some sort of auto-complete on their minds before reaching "HTML document"). Or you can actually have it externally, just like CSS.

#### External Javascript

You just write your script in a file with a **.js** extension and reference it in your HTML document

So it'd be typically like this:

In someFile.js:

```javascript
some javascript code
```

and to reference it in your HTML document, you do so with the ```<script>``` tag in HTML, and you can then put that tag anywhwere in your HTML (If you're not going to ask your mom where it is later). Here's in the ```<head>``` tag:

```html
<!DOCTYPE html>
<html>
<head>
<script src="myScript.js"></script>
</head>
<body>
<h2>Demo JavaScript in Head</h2>

<p id="demo">A Paragraph</p>
<button type="button" onclick="myFunction()">Try it</button>

</body>
</html>
```

and here's inside the ```<body>``` tag:

```html
<!DOCTYPE html>
<html>
<body>

<h2>Demo JavaScript in Body</h2>

<p id="demo">A Paragraph</p>

<button type="button" onclick="myFunction()">Try it</button>

<script src="myScript.js"></script>

</body>
</html>
```

**A VERY BIG IMPORTANT NOTE:**

The browser reads code in the order it appears in the file.

If the JavaScript loads first and it is supposed to affect the HTML that hasn't loaded yet, there could be problems. Placing JavaScript near the bottom of an HTML page is one way to accommodate this dependency.

#### Internal Javascript:

To write JavaScript internally, and I don't know why you would do that, you still write in the ```<script>``` tag and place it accordingly.

```html
<!DOCTYPE html>
<html>
<body>

<h2>Demo JavaScript in Body</h2>

<p id="demo">A Paragraph</p>

<button type="button" onclick="myFunction()">Try it</button>

<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";
}
</script>

</body>
</html>
```

### Variables

You start by declaring a variable with the let keyword, followed by the name you give to the variable:

```javascript
let myVariable;
```

A semicolon at the end of a line indicates where a statement ends. It is only required when you need to separate statements on a single line. However, some people believe it's good practice to have semicolons at the end of each statement. There are other rules for when you should and shouldn't use semicolons. For more details, see [Your Guide to Semicolons in JavaScript.](https://www.codecademy.com/resources/blog/your-guide-to-semicolons-in-javascript/)

And JavaScript is case sensitive in case you didn't know.

After declaring a variable, you can give it a value:

```javascript
myVariable = "Bob";
```

Also, you can do both these operations on the same line:

```javascript
let myVariable = "Bob";
```

You retrieve the value by calling the variable name:

```javascript
myVariable;
```

After assigning a value to a variable, you can change it later in the code:

```javascript
let myVariable = "Bob";
myVariable = "Steve";
```

And of course, variables may hold values that have different [data types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures):

* **[String:](https://developer.mozilla.org/en-US/docs/Glossary/String)** This is a sequence of text known as a string. To signify that the value is a string, enclose it in single or double quote marks.
```javascript
let myVariable = 'Bob';
```

or

```javascript
let myVariable = "Bob";
```

* **[Number:](https://developer.mozilla.org/en-US/docs/Glossary/Number)** This is a number. Numbers don't have quotes around them.

```javascript
let myVariable = 10;
```

* **[Boolean:](https://developer.mozilla.org/en-US/docs/Glossary/Boolean)** This is a True/False value. The words true and false are special keywords that don't need quote marks.

```javascript
let myVariable = true;
```

* **[Array:](https://developer.mozilla.org/en-US/docs/Glossary/Array)** This is a structure that allows you to store multiple values in a single reference.

```javascript
let myVariable = [1,'Bob','Steve',10];
```

And refer to each member of the array like this:

```javascript
myVariable[0], myVariable[1], ...
```

* **[Object:](https://developer.mozilla.org/en-US/docs/Glossary/Object)** This can be anything. Everything in JavaScript is an object and can be stored in a variable. Keep this in mind as you learn.

```javascript
let myVariable = document.querySelector('h1');
```

and all of the above the examples too. And no, I won't even mention ```var``` or the hoisting thing.

#### What about constants?

Just use ```const``` instead of ```let``` and you'll be fine but you MUST give it a value.

### Comments, and you better be writing them

**Single Line:**

```javascript
// This is a comment
```

**Multi-Line**

```javascript
/*
Everything in between is a comment.
*/

```

### Operators

Same as all languages but with a little addition.

* **Strict equality/inequality:** This performs a test to see if two values are **equal** and of the **same data type.** It returns a ```true```/```false``` (Boolean) result.

```javascript
===
```

```javascript
!==
```


### Conditionals

```javascript
if (condition1) {
  statement1;
} else if (condition2) {
  statement2;
} else if (conditionN) {
  statementN;
} else {
  statementLast;
}
```

### Functions

```javascript
function multiply(num1, num2) {
  let result = num1 * num2;
  return result;
}
multiply(4, 7);
multiply(20, 20);
multiply(0.5, 3);

```

#### Functions versus methods
---

**Functions that are part of objects are called methods.**

### Events is where we talkin' business

Real interactivity on a website requires event handlers. These are code structures that listen for activity in the browser, and run code in response. The most obvious example is handling the *click event*, which is fired by the browser when you click on something with your mouse.

```javascript
document.querySelector("html").addEventListener("click", function () {
  alert("Ouch! Stop poking me!");
});
```

There are a number of ways to attach an event handler to an element. Here we select the ```<html>``` element. We then call its ```addEventListener()``` function, passing in the name of the event to listen to (```'click'```) and a function to run when the event happens.

The function we just passed to ```addEventListener()``` here is called an *anonymous function*, because it doesn't have a name. There's an alternative way of writing anonymous functions, which we call an *arrow function*. An arrow function uses ```() =>``` instead of function ```()```:

```javascript
document.querySelector("html").addEventListener("click", () => {
  alert("Ouch! Stop poking me!");
});
```

### JavaScript data types and data structures

JavaScript is a *weakly typed* language, which means it allows implicit type conversion when an operation involves mismatched types, instead of throwing type errors.

```javascript
const foo = 42; // foo is a number
const result = foo + "1"; // JavaScript coerces foo to a string, so it can be concatenated with the other operand
console.log(result); // 421

```

#### Primitive values
---

All types except **Object** define **immutable** values represented directly at the lowest level of the language. We refer to values of these types as *primitive values*.

All primitive types, except ```null```, can be tested by the ```typeof``` operator. ```typeof null``` returns ```"object"```, so one has to use ```=== null``` to test for ```null```.

All primitive types, except ```null``` and ```undefined```, have their corresponding **object wrapper types**, which provide useful methods for working with the primitive values. For example, the ```Number``` object provides methods like ```toExponential()```. When a property is accessed on a primitive value, JavaScript automatically wraps the value into the corresponding wrapper object and accesses the property on the object instead. However, accessing a property on ```null``` or ```undefined``` throws a ```TypeError``` exception.

#### Undefined type
---

Conceptually, ```undefined``` indicates the absence of a value, while ```null``` indicates the absence of an object (which could also make up an excuse for ```typeof null === "object"```). The language usually defaults to ```undefined``` when something is **devoid** of a value:

* A ```return``` statement with no value (```return;```) implicitly returns ```undefined```.

* Accessing a nonexistent object property (```obj.iDontExist```) returns ```undefined```.

* A variable declaration without initialization (```let x;```) implicitly initializes the variable to ```undefined```.

* Many methods, such as ```Array.prototype.find()``` and ```Map.prototype.get()```, return ```undefined``` when no element is found.

```null``` is a keyword, but ```undefined``` is a normal identifier that happens to be a global property. In practice, the difference is minor, since ```undefined``` should not be redefined or shadowed.

#### Number type
---

Something intersting here.

Values outside the range $\{\displaystyle ±(2^{-1074} to 2^{1024})}$ are automatically converted:

* Positive values greater than ```Number.MAX_VALUE``` are converted to ```+Infinity```.
* Positive values smaller than ```Number.MIN_VALUE``` are converted to ```+0```.
* Negative values smaller than ```-Number.MAX_VALUE``` are converted to ```-Infinity```.
* Negative values greater than ```-Number.MIN_VALUE``` are converted to ```-0```.

```0``` is represented as both ```-0``` and ```+0``` (where ```0``` is an alias for ```+0```). In practice, there is almost no difference between the different representations; for example, ```+0 === -0``` is ```true```. However, you are able to notice this when you divide by zero:

```javascript
console.log(42 / +0); // Infinity
console.log(42 / -0); // -Infinity
```

```NaN``` ("Not a Number") is a special kind of number value that's typically encountered when the result of an arithmetic operation cannot be expressed as a number. It is also the only value in JavaScript that is not equal to itself.

#### BigInt type
---

The ```BigInt``` type is a numeric primitive in JavaScript that can represent integers with arbitrary magnitude. With BigInts, you can safely store and operate on large integers even beyond the safe integer limit ```(Number.MAX_SAFE_INTEGER)``` for Numbers.

A BigInt is created by appending ```n``` to the end of an integer or by calling the ```BigInt()``` function.

```javascript
// BigInt
const x = BigInt(Number.MAX_SAFE_INTEGER); // 9007199254740991n
x + 1n === x + 2n; // false because 9007199254740992n and 9007199254740993n are unequal

// Number
Number.MAX_SAFE_INTEGER + 1 === Number.MAX_SAFE_INTEGER + 2; // true because both are 9007199254740992

```

A ```TypeError``` is thrown if ```BigInt``` values are mixed with regular numbers in arithmetic expressions, or if they are implicitly converted to each other.

```BigInt``` is for big number and not fractional numbers.
---

**Very random note:** Use strings for textual data. When representing complex data, parse strings, and use the appropriate abstraction.
---

#### Symbol type
---

A Symbol is a unique and immutable primitive value and may be used as the key of an Object property. In some programming languages, Symbols are called "atoms". The purpose of symbols is to create unique property keys that are guaranteed not to clash with keys from other code.

### Objects

They have the look of Python dictionaries

```javascript
const person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio: function () {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  },
  introduceSelf: function () {
    console.log(`Hi! I'm ${this.name[0]}.`);
  },
};

```

Data items are referred to as the object's **properties**. Functions that allow the object to do something with that data, and are referred to as the object's **methods**.

When the object's members are functions there's a simpler syntax. Instead of bio: function () we can write bio(). Like this:

```javascript
const person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio() {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  },
  introduceSelf() {
    console.log(`Hi! I'm ${this.name[0]}.`);
  },
};

```

An object like this is referred to as an **object literal** — we've literally written out the object contents as we've come to create it. This is different compared to objects instantiated from classes, which we'll look at later on.

It is very common to create an object using an object literal when you want to transfer a series of structured, related data items in some manner, for example sending a request to the server to be put into a database. Sending a single object is much more efficient than sending several items individually, and it is easier to work with than an array, when you want to identify individual items by name.

#### Properties
---

In JavaScript, objects can be seen as a collection of properties. Object properties are equivalent to key-value pairs. Property keys are either strings or symbols. Property values can be values of any type, including other objects, which enables building complex data structures.

There are two types of object properties: The **data property** and the **accessor property**. Each property has corresponding attributes. Each attribute is accessed internally by the JavaScript engine, but you can set them through ```Object.defineProperty()```, or read them through ```Object.getOwnPropertyDescriptor()```.

##### **Data property**
---

Data properties associate a key with a value. It can be described by the following attributes:

```value```

The value retrieved by a get access of the property. Can be any JavaScript value.

```writable```

A boolean value indicating if the property can be changed with an assignment.

```enumerable```

A boolean value indicating if the property can be enumerated by a for...in loop.

```configurable```

A boolean value indicating if the property can be deleted, can be changed to an accessor property, and can have its attributes changed.

##### **Accessor property**
---

Associates a key with one of two accessor functions (```get``` and ```set```) to retrieve or store a value.

**Note:** It's important to recognize it's accessor property — not accessor method. We can give a JavaScript object class-like accessors by using a function as a value — but that doesn't make the object a class.

An accessor property has the following attributes:

```get```

A function called with an empty argument list to retrieve the property value whenever a get access to the value is performed. May be ```undefined```.

```set```

A function called with an argument that contains the assigned value. Executed whenever a specified property is attempted to be changed. May be ```undefined```.

```enumerable```

A boolean value indicating if the property can be enumerated by a for...in loop.

```configurable```

A boolean value indicating if the property can be deleted, can be changed to a data property, and can have its attributes changed.

#### Objects as object properties
---

An object property can itself be an object. For example, try changing the ```name``` member from

```javascript
const person = {
  name: ["Bob", "Smith"],
};

```

to

```javascript
const person = {
  name: {
    first: "Bob",
    last: "Smith",
  },
  // …
};

```

To access these items you just need to chain the extra step onto the end with another dot.

```javascript
person.name.first;
person.name.last;

```

If you do this, you'll also need to go through your method code and change any instances of

```javascript
name[0];
name[1];

```

To

```javascript
name.first;
name.last;

```

Otherwise, your methods will no longer work.

#### Bracket notation
---

Bracket notation provides an alternative way to access object properties. Instead of using dot notation like this:

```javascript
person.age;
person.name.first;

```

You can instead use square brackets:

```javascript
person["age"];
person["name"]["first"];

```

It is no wonder that objects are sometimes called **associative arrays** — they map strings to values in the same way that arrays map numbers to values.

Dot notation is generally preferred over bracket notation because it is more succinct and easier to read. However there are some cases where you have to use square brackets. For example, if an object property name is held in a variable, then you can't use dot notation to access the value, but you can access the value using bracket notation.

In the example below, the ```logProperty()``` function can use ```person[propertyName]``` to retrieve the value of the property named in ```propertyName```.

```javascript
const person = {
  name: ["Bob", "Smith"],
  age: 32,
};

function logProperty(propertyName) {
  console.log(person[propertyName]);
}

logProperty("name");
// ["Bob", "Smith"]
logProperty("age");
// 32

```

#### Setting object members
---

Setting members doesn't just stop at updating the values of existing properties and methods; you can also create completely new members.

```javascript
person["eyes"] = "hazel";
person.farewell = function () {
  console.log("Bye everybody!");
};

```

One useful aspect of bracket notation is that it can be used to set not only member values dynamically, but member names too. Let's say we wanted users to be able to store custom value types in their people data, by typing the member name and value into two text inputs. We could get those values like this:

```javascript
const myDataName = nameInput.value;
const myDataValue = nameValue.value;

```

We could then add this new member name and value to the ```person``` object like this:

```javascript
person[myDataName] = myDataValue;

```

Adding a property to an object using the method above isn't possible with dot notation, which can only accept a literal member name, not a variable value pointing to a name.

#### Introducing constructors
---

A constructor is just a function called using the ```new``` keyword. When you call a constructor, it will:

* create a new object
* bind ```this``` to the new object, so you can refer to ```this``` in your constructor code
* run the code in the constructor
* return the new object.

Constructors, by convention, start with a capital letter and are named for the type of object they create.

```javascript
function Person(name) {
  this.name = name;
  this.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
}

```

To call ```Person()``` as a constructor, we use ```new```:

```javascript
const salva = new Person("Salva");
salva.name;
salva.introduceSelf();
// "Hi! I'm Salva."

const frankie = new Person("Frankie");
frankie.name;
frankie.introduceSelf();
// "Hi! I'm Frankie."

```

#### Object prototypes
---

Prototypes are the mechanism by which JavaScript objects inherit features from one another.

#### The prototype chain
---

```javascript
const myObject = {
  city: "Madrid",
  greet() {
    console.log(`Greetings from ${this.city}`);
  },
};

myObject.greet(); // Greetings from Madrid
```

This is an object with one data property, ```city```, and one method, ```greet()```. If you type the object's name followed by a period into the console, like ```myObject.```, then the console will pop up a list of all the properties available to this object. You'll see that as well as ```city``` and gr```eet, there are lots of other properties!

```javascript
__defineGetter__
__defineSetter__
__lookupGetter__
__lookupSetter__
__proto__
city
constructor
greet
hasOwnProperty
isPrototypeOf
propertyIsEnumerable
toLocaleString
toString
valueOf
```

Try accessing one of them:

```javscript
myObject.toString(); // "[object Object]"

```

works just fine.

Every object in JavaScript has a built-in property, which is called its **prototype**. The prototype is itself an object, so the prototype will have its own prototype, making what's called a **prototype chain**. The chain ends when we reach a** prototype that has null for its own prototype**.

**Note:** The property of an object that points to its prototype is not called ```prototype```. Its name is not standard, but in practice all browsers use ```__proto__```. The standard way to access an object's prototype is the ```Object.getPrototypeOf()``` method.

When you try to access a property of an object: if the property can't be found in the object itself, the prototype is searched for the property. If the property still can't be found, then the prototype's prototype is searched, and so on until either the property is found, or the end of the chain is reached, in which case ```undefined``` is returned.

So when we call ```myObject.toString()```, the browser:

* looks for ```toString``` in ```myObject```
* can't find it there, so looks in the prototype object of ```myObject``` for ```toString```
* finds it there, and calls it.


What is the prototype for ```myObject```? To find out, we can use the function ```Object.getPrototypeOf()```:

```javascript
Object.getPrototypeOf(myObject); // Object { }
```

This is an object called ```Object.prototype```, and it is the most basic prototype, that all objects have by default. The prototype of ```Object.prototype``` is ```null```, so it's at the end of the prototype chain:

![protochain](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes/myobject-prototype-chain.svg)

The prototype of an object is not always ```Object.prototype```. Try this:

```javascript
const myDate = new Date();
let object = myDate;

do {
  object = Object.getPrototypeOf(object);
  console.log(object);
} while (object);

// Date.prototype
// Object { }
// null

```

This code creates a ```Date``` object, then walks up the prototype chain, logging the prototypes. It shows us that the prototype of ```myDate``` is a ```Date.prototype``` object, and the prototype of that is ```Object.prototype```.

![protochain2](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes/mydate-prototype-chain.svg)

In fact, when you call familiar methods, like ```myDate2.getMonth()```, you are calling a method that's defined on ```Date.prototype```.

#### Setting a prototype
---

##### Using ```Object.create```
---

The ```Object.create()``` method creates a new object and allows you to specify an object that will be used as the new object's prototype.

```javascript
const personPrototype = {
  greet() {
    console.log("hello!");
  },
};

const carl = Object.create(personPrototype);
carl.greet(); // hello!

```

Here we create an object ```personPrototype```, which has a ```greet()``` method. We then use ```Object.create()``` to create a new object with ```personPrototype``` as its prototype. Now we can call ```greet()``` on the new object, and the prototype provides its implementation.

##### Using a constructor
---

In JavaScript, all functions have a property named ```prototype```. When you call a function as a constructor, this property is set as the prototype of the newly constructed object (by convention, in the property named ```__proto__```).

So if we set the ```prototype``` of a constructor, we can ensure that all objects created with that constructor are given that prototype:

```javascript
const personPrototype = {
  greet() {
    console.log(`hello, my name is ${this.name}!`);
  },
};

function Person(name) {
  this.name = name;
}

Object.assign(Person.prototype, personPrototype);
// or
// Person.prototype.greet = personPrototype.greet;

```

Here we create:

* an object ```personPrototype```, which has a ```greet()``` method
* a ```Person()``` constructor function which initializes the name of the person to create.

We then put the methods defined in ```personPrototype``` onto the Person function's prototype property using ```Object.assign```.

After this code, objects created using ```Person()``` will get ```Person.prototype``` as their prototype, which automatically contains the ```greet``` method.

```javascript
const reuben = new Person("Reuben");
reuben.greet(); // hello, my name is Reuben!
```

This also explains why we said earlier that the prototype of ```myDate``` is called ```Date.prototype```: it's the prototype property of the ```Date``` constructor.

##### Own properties
---

The objects we create using the ```Person``` constructor above have two properties:

* a ```name``` property, which is set in the **constructor**, so it appears directly on ```Person``` objects
* a ```greet()``` method, which is set in the **prototype**.


It's common to see this pattern, in which **methods are defined on the prototype, but data properties are defined in the constructor.** That's because *methods are usually the same for every object we create, while we often want each object to have its own value for its data properties* (just as here where every person has a different name).

Properties that are defined *directly in the object*, like name here, are called **own properties**, and you can check whether a property is an own property using the static ```Object.hasOwn()``` method:

```javascript
const irma = new Person("Irma");

console.log(Object.hasOwn(irma, "name")); // true
console.log(Object.hasOwn(irma, "greet")); // false

```

### Indexed collections: Arrays and typed Arrays

Arrays are regular objects for which there is a particular relationship between integer-keyed properties and the ```length``` property.

Additionally, arrays inherit from ```Array.prototype```, which provides a handful of convenient methods to manipulate arrays. For example, ```indexOf()``` searches a value in the array and ```push()``` appends an element to the array. This makes Arrays a perfect candidate to represent ordered lists.

Typed Arrays present an array-like view of an underlying binary data buffer, and offer many methods that have similar semantics to the array counterparts. "Typed array" is an umbrella term for a range of data structures, including ```Int8Array```, ```Float32Array```, etc.

### Keyed collections: Maps, Sets, WeakMaps, WeakSets

These data structures take object references as keys. ```Set``` and ```WeakSet``` represent a collection of **unique** values, while ``Map`` and ``WeakMap`` represent a collection of **key-value associations**.

```Maps``` and ```WeakMaps``` make it easy to *privately* bind data to an object.

```WeakMap``` and ```WeakSet``` only allow **garbage-collectable** values as keys, which are either **objects or non-registered symbols**, and the keys may be collected even when they remain in the collection. They are specifically used for **memory usage optimization**.

### Type coercion

JavaScript is a weakly typed language. This means that you can often use a value of one type where another type is expected, and the language will convert it to the right type for you.

#### Primitive coercion
---

The primitive coercion process is used where a primitive value is expected, but there's no strong preference for what the actual type should be. This is usually when a string, a number, or a BigInt are equally acceptable. For example:

* The ```Date()``` constructor, when it receives one argument that's not a ```Date``` instance — **strings represent date strings, while numbers represent timestamps.**

* The ```+``` operator — if one operand is a string, string concatenation is performed; otherwise, numeric addition is performed.

* The ```==``` operator — if one operand is a primitive while the other is an object, the object is converted to a primitive value with no preferred type.

This operation does not do any conversion if the value is already a primitive.

#### Numeric coercion
---

Numeric coercion is nearly the same as number coercion, except that BigInts are returned as-is instead of causing a ```TypeError```. Numeric coercion is used by all arithmetic operators, since they are overloaded for both numbers and BigInts. The only exception is unary plus, which always does number coercion.

All data types, except Null, Undefined, and Symbol, have their respective coercion process.

### Operator Precedence

Highest to lowest

<table class="fullwidth-table" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
  <tbody speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <th speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Precedence</th>
      <th speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Operator type</th>
      <th speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Associativity</th>
      <th speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Individual operators</th>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">18</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Grouping" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Grouping</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">n/a</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">( … )</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td rowspan="5" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">17</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#dot_notation" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Member Access</a></td>
      <td rowspan="2" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… . …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Optional chaining</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… ?. …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#bracket_notation" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Computed Member
                Access</a></td>
      <td rowspan="3" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">n/a</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… [ … ]</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/new" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">new</code></a> (with argument list)</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">new … ( … )</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Guide/Functions" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Function Call</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… ( … )</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">16</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/new" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">new</code></a> (without argument list)</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">n/a</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">new …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td rowspan="2" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">15</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators#increment_and_decrement" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Postfix
                Increment</a></td>
      <td rowspan="2" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">n/a</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… ++</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators#increment_and_decrement" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Postfix
                Decrement</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… --</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td rowspan="10" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">14</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Logical NOT (!)</a></td>
      <td rowspan="10" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">n/a</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">! …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_NOT" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Bitwise NOT (~)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">~ …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Unary plus (+)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">+ …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Unary negation (-)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">- …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators#increment_and_decrement" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Prefix
                Increment</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">++ …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators#increment_and_decrement" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Prefix
                Decrement</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">-- …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/typeof" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">typeof</code></a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">typeof …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/void" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">void</code></a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">void …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/delete" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">delete</code></a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">delete …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/await" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">await</code></a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">await …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">13</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Exponentiation (**)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">right-to-left</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… ** …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td rowspan="3" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">12</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Multiplication (*)</a></td>
      <td rowspan="3" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… * …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Division" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Division (/)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… / …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Remainder" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Remainder (%)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… % …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td rowspan="2" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">11</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Addition" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Addition (+)</a></td>
      <td rowspan="2" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… + …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Subtraction (-)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… - …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td rowspan="3" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">10</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Bitwise Left Shift (&lt;&lt;)</a></td>
      <td rowspan="3" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &lt;&lt; …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Bitwise Right Shift (&gt;&gt;)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &gt;&gt; …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Bitwise Unsigned Right Shift (&gt;&gt;&gt;)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &gt;&gt;&gt; …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td rowspan="6" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">9</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Less_than" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Less Than (&lt;)</a></td>
      <td rowspan="6" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &lt; …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Less_than_or_equal" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Less Than Or Equal (&lt;=)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &lt;= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Greater Than (&gt;)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &gt; …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Greater Than Or Equal (&gt;=)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &gt;= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/in" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">in</code></a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… in …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/instanceof" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">instanceof</code></a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… instanceof …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td rowspan="4" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">8</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Equality" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Equality (==)</a></td>
      <td rowspan="4" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… == …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Inequality" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Inequality (!=)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… != …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Strict Equality (===)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… === …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Strict Inequality (!==)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… !== …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">7</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Bitwise AND (&amp;)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &amp; …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">6</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Bitwise XOR (^)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… ^ …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">5</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_OR" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Bitwise OR (|)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… | …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">4</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Logical AND (&amp;&amp;)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &amp;&amp; …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td rowspan="2" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">3</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Logical OR (||)</a></td>
      <td rowspan="2" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… || …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Nullish coalescing operator (??)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… ?? …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td rowspan="21" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">2</td>
      <td rowspan="16" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators#assignment_operators" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Assignment</a></td>
      <td rowspan="16" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">right-to-left</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… = …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… += …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… -= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… **= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… *= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… /= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… %= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &lt;&lt;= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &gt;&gt;= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &gt;&gt;&gt;= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &amp;= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… ^= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… |= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… &amp;&amp;= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… ||= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… ??= …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Conditional (ternary) operator</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">right-to-left<br speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">(Groups on expressions after <code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">?</code>)</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… ? … : …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Arrow (=&gt;)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">right-to-left</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… =&gt; …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/yield" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">yield</code></a></td>
      <td rowspan="3" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">n/a</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">yield …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/yield*" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">yield*</code></a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">yield* …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Spread (...)</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">... …</code></td>
    </tr>
    <tr speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">1</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><a href="/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator" speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">Comma / Sequence</a></td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px">left-to-right</td>
      <td speechify-initial-font-family="Inter, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif" speechify-initial-font-size="16px"><code speechify-initial-font-family="Menlo, Consolas, Monaco, &quot;Liberation Mono&quot;, &quot;Lucida Console&quot;, monospace" speechify-initial-font-size="13.328px">… , …</code></td>
    </tr>
  </tbody>
</table>

### Short-circuiting

we said "the higher-precedence expressions are always evaluated first" — this is generally true, but it has to be amended with the acknowledgement of short-circuiting, in which case an operand may not be evaluated at all.

Short-circuiting is jargon for conditional evaluation. For example, in the expression ```a && (b + c)```, if ```a``` is falsy, then the sub-expression ```(b + c)``` will not even get evaluated, even if it is grouped and therefore has higher precedence than ```&&```. We could say that the logical ```AND``` operator (```&&```) is "short-circuited". Along with logical ```AND```, other short-circuited operators include logical ```OR``` (```||```), nullish coalescing (```??```), and optional chaining (```?.```).

```javascript
a || (b * c); // evaluate `a` first, then produce `a` if `a` is "truthy"
a && (b < c); // evaluate `a` first, then produce `a` if `a` is "falsy"
a ?? (b || c); // evaluate `a` first, then produce `a` if `a` is not `null` and not `undefined`
a?.b.c; // evaluate `a` first, then produce `undefined` if `a` is `null` or `undefined`
```

When evaluating a short-circuited operator, the left operand is always evaluated. The right operand will only be evaluated if the left operand cannot determine the result of the operation.

### Block statement

The most basic statement is a block statement, which is used to group statements. The block is delimited by a pair of curly braces:

```javascript
{
  statement1;
  statement2;
  // …
  statementN;
}

```

### Falsy values

* ```false```
* ```undefined```
* ```null```
* ```0```
* ```NaN```
* ```the empty string (```""```)

### switch statement

```javascript
switch (expression) {
  case label1:
    statements1;
    break;
  case label2:
    statements2;
    break;
  // …
  default:
    statementsDefault;
}
```

### throw statement

Use the ```throw``` statement to throw an exception. A throw statement specifies the value to be thrown:

```javascript
throw "Error2"; // String type
throw 42; // Number type
throw true; // Boolean type
throw {
  toString() {
    return "I'm an object!";
  },
};

```

### ```try...catch...finally``` statement

```javascript
function f() {
  try {
    throw "bogus";
  } catch (e) {
    console.log('caught inner "bogus"');
    // This throw statement is suspended until
    // finally block has completed
    throw e;
  } finally {
    return false; // overwrites the previous "throw"
  }
  // "return false" is executed now
}

try {
  console.log(f());
} catch (e) {
  // this is never reached!
  // while f() executes, the `finally` block returns false,
  // which overwrites the `throw` inside the above `catch`
  console.log('caught outer "bogus"');
}

// Logs:
// caught inner "bogus"
// false

```

### Utilizing Error objects

Depending on the type of error, you may be able to use the ```name``` and ```message``` properties to get a more refined message.

The ```name``` property provides the general class of Error (such as ```DOMException``` or ```Error```), while ```message``` generally provides a more succinct message than one would get by converting the error object to a string.

If you are throwing your own exceptions, in order to take advantage of these properties (such as if your ```catch``` block doesn't discriminate between your own exceptions and system ones), you can use the ```Error``` constructor.

```javascript
function doSomethingErrorProne() {
  if (ourCodeMakesAMistake()) {
    throw new Error("The message");
  } else {
    doSomethingToGetAJavaScriptError();
  }
}

try {
  doSomethingErrorProne();
} catch (e) {
  // Now, we actually use `console.error()`
  console.error(e.name); // 'Error'
  console.error(e.message); // 'The message', or a JavaScript error message
}

```

---

*Random notes for my somewhat forgetful self:*

This feature - when a method has the **same name but a different implementation in different classes** - is called **polymorphism**. When a method in a subclass replaces the superclass's implementation, we say that the subclass **overrides** the version in the superclass.
---

Objects provide an interface to other code that wants to use them but maintain their own internal state. The object's internal state is kept **private**, meaning that it can only be accessed by the object's own methods, not from other objects. Keeping an object's internal state private, and generally making a clear division between its public interface and its private internal state, is called **encapsulation**.
---

## OOP and JavaScript

First, in class-based OOP, classes and objects are two separate constructs, and objects are always created as instances of classes. Also, there is a distinction between the feature used to define a class (the class syntax itself) and the feature used to instantiate an object (a constructor). In JavaScript, we can and often do create objects without any separate class definition, either using a function or an object literal. This can make working with objects much more lightweight than it is in classical OOP.

Second, although a prototype chain looks like an inheritance hierarchy and behaves like it in some ways, it's different in others. When a subclass is instantiated, a single object is created which combines properties defined in the subclass with properties defined further up the hierarchy. With prototyping, each level of the hierarchy is represented by a separate object, and they are linked together via the ```__proto__``` property. The prototype chain's behavior is less like inheritance and more like delegation. Delegation is a programming pattern where an object, when asked to perform a task, can perform the task itself or ask another object (its delegate) to perform the task on its behalf. In many ways, delegation is a more flexible way of combining objects than inheritance (for one thing, it's possible to change or completely replace the delegate at run time).

That said, constructors and prototypes can be used to implement class-based OOP patterns in JavaScript. But using them directly to implement features like inheritance is tricky, so JavaScript provides extra features, layered on top of the prototype model, that map more directly to the concepts of class-based OOP.

### Classes in JavaScript

#### Classes and constructors
---

You can declare a class using the ```class``` keyword. Here's a class declaration for our ```Person```:

```javascript
class Person {
  name;

  constructor(name) {
    this.name = name;
  }

  introduceSelf() {
    console.log(`Hi! I'm ${this.name}`);
  }
}

```

The ```name;``` declaration is optional: you could omit it, and the line ```this.name = name;``` in the constructor will create the ```name``` property before initializing it. However, listing properties explicitly in the class declaration might make it easier for people reading your code to see which properties are part of this class.

You could also initialize the property to a default value when you declare it, with a line like ```name = '';```.

##### Omitting constructors
---

If you don't need to do any special initialization, you can omit the constructor, and a default constructor will be generated for you:

```javascript
class Animal {
  sleep() {
    console.log("zzzzzzz");
  }
}

const spot = new Animal();

spot.sleep(); // 'zzzzzzz'

```

#### Inheritance

Given our ```Person``` class above, let's define the ```Professor``` subclass.

```javascript
class Professor extends Person {
  teaches;

  constructor(name, teaches) {
    super(name);
    this.teaches = teaches;
  }

  introduceSelf() {
    console.log(
      `My name is ${this.name}, and I will be your ${this.teaches} professor.`,
    );
  }

  grade(paper) {
    const grade = Math.floor(Math.random() * (5 - 1) + 1);
    console.log(grade);
  }
}

```

We use the ```extends``` keyword to say that this class inherits from another class.

The ```Professor``` class adds a new property ```teaches```, so we declare that.

Since we want to set ```teaches``` when a new ```Professor``` is created, we define a constructor, which takes the ```name``` and ```teaches``` as arguments. The first thing this constructor does is call the superclass constructor using ```super()```, passing up the ```name``` parameter. The superclass constructor takes care of setting ```name```. After that, the ```Professor``` constructor sets the ```teaches``` property.

We've also overridden the ```introduceSelf()``` method from the superclass, and added a new method ```grade()```, to grade a paper

**Note:** If a subclass has any of its own initialization to do, it must first call the superclass constructor using super(), passing up any parameters that the superclass constructor is expecting.

#### Encapsulation

```javascript
class Student extends Person {
  #year;

  constructor(name, year) {
    super(name);
    this.#year = year;
  }

  introduceSelf() {
    console.log(`Hi! I'm ${this.name}, and I'm in year ${this.#year}.`);
  }

  canStudyArchery() {
    return this.#year > 1;
  }
}

```

In this class declaration, ```#year``` is a private data property. We can construct a ```Student``` object, and it can use ```#year``` internally, but if code outside the object tries to access ```#year``` the browser throws an error:

```javascript
const summers = new Student("Summers", 2);

summers.introduceSelf(); // Hi! I'm Summers, and I'm in year 2.
summers.canStudyArchery(); // true

summers.#year; // SyntaxError

```

Private data properties must be declared in the class declaration, and their names start with ```#```.

Same thing applies to when you want to have a **private method**, their names start with #, and they can only be called by the object's own methods:

```javascript
class Example {
  somePublicMethod() {
    this.#somePrivateMethod();
  }

  #somePrivateMethod() {
    console.log("You called me?");
  }
}

const myExample = new Example();

myExample.somePublicMethod(); // 'You called me?'

myExample.#somePrivateMethod(); // SyntaxError

```

**Note:** Code run in the Chrome console can access private properties outside the class. This is a DevTools-only relaxation of the JavaScript syntax restriction.

## Working with JSON

### Arrays as JSON

We can convert arrays to/from JSON. Below is also valid JSON, for example:

```javascript
[
  {
    "name": "Molecule Man",
    "age": 29,
    "secretIdentity": "Dan Jukes",
    "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
  },
  {
    "name": "Madame Uppercut",
    "age": 39,
    "secretIdentity": "Jane Wilson",
    "powers": [
      "Million tonne punch",
      "Damage resistance",
      "Superhuman reflexes"
    ]
  }
]

```

The above is perfectly valid JSON. You'd just have to access array items (in its parsed version) by starting with an array index, for example ```[0]["powers"][0]```.

---

**Notes:**

* JSON is purely a string with a specified data format — it contains only properties, no methods.

* JSON requires double quotes to be used around strings and property names. Single quotes are not valid other than surrounding the entire JSON string.

* JSON can actually take the form of any data type that is valid for inclusion inside JSON, not just arrays or objects. So for example, a single string or number would be valid JSON.

* Unlike in JavaScript code in which object properties may be unquoted, in JSON only quoted strings may be used as properties.

### Converting between objects and text

sometimes we aren't so lucky — sometimes we receive a raw JSON string, and we need to convert it to an object ourselves. And when we want to send a JavaScript object across the network, we need to convert it to JSON (a string) before sending it. Luckily, these two problems are so common in web development that a built-in JSON object is available in browsers, which contains the following two methods:

* ```parse()```: Accepts a **JSON string** as a parameter, and returns the corresponding **JavaScript object**.

* ```stringify()```: Accepts an **object** as a parameter, and returns the equivalent **JSON string**.

## Modules

[This is an awesome link](https://darrenderidder.github.io/talks/ModulePatterns/#/1)
