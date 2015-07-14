var router = require('express').Router()
var request = require('request')
var io

router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' })
})

router.get('/register', function(req, res, next) {
  io = req.app.get('socketio')
  
  io.on('connection', function(socket) {
    console.log('server side connected')
  
    socket.on('send', function(user, text) {
      console.log(user, text)
      request({
        method: 'POST',
        url: 'http://localhost:8000/api/v1/external/received/5983ac6c-90ab-4097-94e4-2bdd44671779/',
        qs: {
          from: user,
          text: text
        },
        headers: { 'Content-Type': 'text/plain' },
      })
    })

  })

  res.render('register')
})

router.post('/ureceive', function(req, res) {
  console.log(req);
  io = req.app.get('socketio')
  io.emit('message', req.body.text)
  res.send(req.body.text)
})

module.exports = router
