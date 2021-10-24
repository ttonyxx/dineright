const express = require('express');
const pg = require('pg');
const { Pool } = require('pg');
const CockroachDB = require('./CockroachDB');
const responses = require('./responses');

const CONNECTION_PASSWORD = 'prD2DijJDornCKuh';
const CONNECTION_STRING = `postgresql://arjun:${CONNECTION_PASSWORD}@free-tier4.aws-us-west-2.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=./root.crt&options=--cluster%3Dtan-hare-712`;

const db = new CockroachDB(CONNECTION_STRING);

const app = express();
app.use(express.json());

app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Headers', 'content-type,authorization');
  res.setHeader('Access-Control-Allow-Methods', 'GET,HEAD,PUT,PATCH,POST,DELETE');
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  if (req.headers.origin)
    res.setHeader('Access-Control-Allow-Origin', req.headers.origin);

  next();
});

app.post('/create-account', async (req, res) => {
  let { email, password, name } = req.body;
  if (!email || !password || !name) {
    return res.send(responses.error('incomplete body'));
  }
  
  // insert data into cockroach for use later
  await db.insert('accounts', {
    email,
    name,
    password
  });

  res.send(responses.success('Account created'));
});

app.post('/valid-user', async (req, res) => {
  let { email, password } = req.body;
  if (!email || !password) {
    return res.send(responses.error('you suck and are a terrible human being'));
  }

  let r = await db.query('SELECT * FROM accounts WHERE email = $1 AND password = $2', [email, password]);
  if (r.rows.length !== 0) {
    return res.send(responses.success( r.rows[0] ));
  }
  return res.send(responses.error());
});

app.all('*', (_, res) => {
  res.send({ success: false, error: 'not found' });
});

app.listen(8080, () => {
  console.log('Server has started!');
});

db.query('SELECT * FROM accounts').then(res => {
  console.log(res.rows);
});
