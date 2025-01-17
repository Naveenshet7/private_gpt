css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/PWKDgW4/photo1700922212.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/2yQwBsZ/images.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
#<a href="https://ibb.co/zrsqD0Q"><img src="https://i.ibb.co/zrsqD0Q/20221029210938-2.jpg" alt="20221029210938-2" border="0" /></a>
#https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png