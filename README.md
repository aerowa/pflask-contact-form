# pflask-contact-form
Python Flask contact form server


Swarm:
```
docker-compose build
docker stack deploy -c docker-compose.yml contact-form-server
```

Docker:
```
docker-compose build
docker-compose up -d
```

### Usage
Form:

```html

  <div id="contact-form">
  <h2>Contact Us</h2>
  <form>
    <div>
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" required>
    </div>
    <div>
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required>
    </div>
    <div>
      <label for="phone">Phone:</label>
      <input type="tel" id="phone" name="phone">
    </div>
    <div>
      <label for="message">Message:</label>
      <textarea id="message" name="message" required></textarea>
    </div>
    <button type="submit">Send</button>
  </form>
</div>
```
JS:

```js
const form = document.querySelector('#contact-form form');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(form);

  fetch('http://your-flask-server-url:3099/contact', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(Object.fromEntries(formData))
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // do something on successful submission
  })
  .catch(error => {
    console.error(error);
    // do something on submission error
  });
});
```
