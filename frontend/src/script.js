import 'https://cdn.jsdelivr.net/npm/vue/dist/vue.js';

var chat = document.createElement('div');
chat.innerHTML = `
<div class="chatbox">
  <div class="chatbox-header">
    <div class="chatbox-agent">
      <span>Chatbot</span>
    </div>
    <div class="chatbox-close">
      <span>x</span>
    </div>
  </div>
  <ul class="chatbox-conversation" id="conversation">
    <li class="chatbox-conversation__message" v-for="message in conversation" v-bind:class="'chatbox-conversation__message--' + message.type">
      <div class="chatbox-message__sender">
        <span>{{ message.sender }}</span>
        <img class="chatbox-message__photo" :src="message.photo">
      </div>
      <div class="chatbox-message__content">
        <p>{{ message.text }}</p>
      </div>
    </li>
  </ul>
  <form class="chatbox-footer">
    <input class="chatbox-message" v-model="message">
    <button type="button" class="chatbox-btn chatbox-btn--send" @click="addMessage()">Send</button>
  </form>
</div>`;
chat.id = "maintel-chat";
document.body.appendChild(chat);

// Event handling code, allowing the ability to bind to specific events.
var Chatbot = {
    events: {},
    on: function(event, callback) {
        var handlers = this.events[event] || [];
        handlers.push(callback);
        this.events[event] = handlers;
    },
    trigger: function(event, data) {
        var handlers = this.events[event];
        if (!handlers || handlers.length < 1)
            return;
        [].forEach.call(handlers, function(handler){
            handler(data);
        });
    }
};

// The Vue instance, mainly used to make data binding easier for now and to see if we can use it inline.
var app = new Vue({
  el: '#maintel-chat',
  data: {
    message: 'So whatttt?',
    conversation: [
      {
        id: 1,
        sender: 'Myself',
        text: 'Hello',
        type: 'to',
        photo: './assets/avatar.png'
      },
      {
        id: 4,
        sender: 'Trump',
        text: 'Make data great again !',
        type: 'from',
        photo: './assets/trump.png'
      }
    ]
  },
  updated: function() {
    var chatConversation = document.getElementById('conversation');
    chatConversation.scrollTop = chatConversation.scrollHeight;
  },
  methods: {
    addMessage: async function() {      
      var messageDetails = {
        id: this.conversation.length + 1,
        sender: 'Myslef',
        text: this.message,
        type: 'to', photo: './assets/avatar.png'
      };
      
      if(this.message.length) {
        this.conversation.push(messageDetails);
        // This code is triggering the 'sendMessage' event and passing in the message data.
        const settings = {
          method: 'POST',
          headers: {
              Accept: 'application/json',
              'Content-Type': 'application/json',
              'Origin':'*'
          },
          mode: 'no-cors',
          body: JSON.stringify({"input": this.message})
      };


      Chatbot.trigger('sendMessage', JSON.parse(JSON.stringify(this.conversation[this.conversation.length-1])));
      try {
        console.log("test")
        const fetchResponse = await fetch(`http://localhost:1880/chatbot/`, settings);
        const data = await fetchResponse.json();
        console.log(data)
        this.message = '';
        return data;
      } catch (e) {
          return e;
      }
      }
    }
  }
});