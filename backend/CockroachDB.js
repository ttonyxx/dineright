const { Pool, Client } = require('pg');
const fs = require('fs');
const parse = require("pg-connection-string").parse;

class CockroachDB {
  constructor(connectionString) {
    let config = parse(connectionString);
    config.port = 26257;
    config.database = 'dineright';

    this.client = new Client(config);
    this.client.connect().then(res => {
      this.init(fs.readFileSync('./dbinit.sql').toString());
    });
  }

  init(sql) {
    let split = sql.split(';').map(e => e.trim());

    for (let i = 0; i < split.length; i++) {
      if (!split[i])
        continue;

      this.query(split[i], []).then(val => {
        // console.log(val)
      }).catch(err => {
        console.log(err);
        process.exit(1);
      });
    }
  }

  insert(table, obj) {
    let values = [];
    let questions = '';
    let keys = '';

    let i = 0;
    for (let key in obj) {
      keys += key + ', ';
      questions += `$${++i}, `;
      values.push(obj[key]);
    }

    keys = keys.substring(0, keys.length - 2);
    questions = questions.substring(0, questions.length - 2);

    return this.query(`INSERT INTO ${table} (${keys}) VALUES (${questions})`, values);
  }

  query(query, args) {
    return this.client.query(query, args);
  }
}

module.exports = CockroachDB;