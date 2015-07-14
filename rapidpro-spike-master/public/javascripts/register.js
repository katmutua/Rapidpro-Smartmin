var user = generateUser()
var socket = io()

function generateUser() {
  return parseInt(Math.random()*100000)  
}

function getUserSubmission() {
  return $('.text').val() 
}

function appendMessage(text, side) {
  $('.messages').append('<li class="msg-' + side + '">' + text + '</li>')  
}

function clearTextAndFocus() {
  $('.text').val('').focus()
}

$('#register').on('submit', function(e) {
  e.preventDefault()
  var text = getUserSubmission()
  appendMessage(text, 'right')
  clearTextAndFocus()
  socket.emit('send', user, text)
})

$(function(){
  socket.emit('send', user, 'register')
})

socket.on('connect', function() {
  console.log('client side connected')
})

socket.on('message', function(message) {
  appendMessage(message, 'left')
})