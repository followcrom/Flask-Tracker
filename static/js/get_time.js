function getTimeOfDayGreeting() {
    var myDate = new Date();
    var timeOfDay = myDate.getHours();
    var greeting = '';
  
    if (timeOfDay >= 6 && timeOfDay < 12) {
      greeting = 'Good morning';
    } else if (timeOfDay >= 12 && timeOfDay < 19) {
      greeting = 'Good afternoon';
    } else if (timeOfDay >= 19 && timeOfDay < 24) {
      greeting = 'Good evening';
    } else {
      greeting = 'Hi Night Owl';
    }
  
    var message = `// ${greeting} // Please visit us at <a href="https://followcrom.online/" class="top">followcrom.online</a>`;
    return message;
  }
  

  var greetingMessage = getTimeOfDayGreeting();
  document.write(greetingMessage);