#!/usr/bin/node

// Script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(response.body);
    const tasksCompleted = {};

    tasks.forEach((task) => {
      if (task.completed) {
        tasksCompleted[task.userId] = (tasksCompleted[task.userId] || 0) + 1;
      }
    });

    console.log(tasksCompleted);
  }
});
