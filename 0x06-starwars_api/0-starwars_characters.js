#!/usr/bin/node

const request = require('request');
const id = process.argv.slice(2)[0];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const options = { json: true };

request(url, options, async (error, response, body) => {
  if (error) console.log('error:', error);
  if (!error && response.statusCode === 200) {
    for (let c = 0; c < body.characters.length; c++) {
      await sleep(500);
      request(body.characters[c], options, (err, resp, bdy) => {
        if (err) console.log('error:', error);
        if (!err && resp.statusCode === 200) {
          console.log(bdy.name);
        }
      });
    }
  }
});

function sleep (ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}
