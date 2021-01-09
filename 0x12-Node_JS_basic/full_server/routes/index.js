const express = require('express');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

const app = express();

router.get('/', ((req, res) => AppController.getHomepage(req, res)));
router.get('/students', ((req, res) => StudentsController.getAllStudents(req, res)));
router.get('/students/:major', ((req, res) => StudentsController.getAllStudentsByMajor(req, res)));

app.listen(1245);

module.exports = app;
