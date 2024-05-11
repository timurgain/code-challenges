require('dotenv').config();

global.myGlobalVariable = 'Hello, World!';

global.SECRET_TOKEN = process.env.SECRET_TOKEN;
