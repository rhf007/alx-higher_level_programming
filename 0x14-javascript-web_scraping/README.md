# JavaScript - Web scraping

I've been waiting for this!

## How to manipulate JSON data & How to use request and fetch API

[This article](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) is good and also because I'm on short on time

## How to read and write a file using fs module

### Reading Files

```javascript
const fs = require('fs').promises;

async function readFile(filePath) {
  try {
    const data = await fs.readFile(filePath);
    console.log(data.toString());
  } catch (error) {
    console.error(`Got an error trying to read the file: ${error.message}`);
  }
}
```

### Writing Files

```javascript
const fs = require('fs').promises;

async function openFile() {
  try {
    const csvHeaders = 'name,quantity,price'
    await fs.writeFile('groceries.csv', csvHeaders);
  } catch (error) {
    console.error(`Got an error trying to write to a file: ${error.message}`);
  }
}
```

### Deleting Files

```javascript
const fs = require('fs').promises;

async function deleteFile(filePath) {
  try {
    await fs.unlink(filePath);
    console.log(`Deleted ${filePath}`);
  } catch (error) {
    console.error(`Got an error trying to delete the file: ${error.message}`);
  }
}

deleteFile('groceries.csv');
```

### Moving Files

```javascript
const fs = require('fs').promises;

async function moveFile(source, destination) {
  try {
    await fs.rename(source, destination);
    console.log(`Moved file from ${source} to ${destination}`);
  } catch (error) {
    console.error(`Got an error trying to move the file: ${error.message}`);
  }
}

moveFile('greetings-2.txt', 'test-data/salutations.txt');
```

## Asynchronous Programming

Because we need to go over that.

[https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing)

[https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises)
