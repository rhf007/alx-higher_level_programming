#!/usr/bin/node

const r = require('request');
const todos = 'https://jsonplaceholder.typicode.com/todos';
let comp = 0;
const user_comp = {};

r.get(todos, function (err, res, bod) {
  if (err) {
    console.log(err);
  } else {
    bod = JSON.parse(bod);
    for (let i = 0; i < bod.length; i++) {
        let usr_id = bod[i].userId;
	let task_stat = bod[i].completed;

	if (task_stat === true && !user_comp[usr_id]) {
          user_comp[usr_id] = 0;
	}

	if (task_stat == true) {
          user_comp[usr_id]++;
	}

	console.log(user_comp);
    }
  }
});
