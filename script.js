
for (let script in scripts) {
  console.log(scripts);

  // onmouseenter="$(this).css('transition','background-position 0ms');"
  // onmouseleave="$(this).css('transition','background-position 450ms');$(this).css('--background-position-x','0%');$(this).css('--background-position-y','0%');"
  // onmouseout="
  //   $(this).animate({
  //     'background-position-x' : '0%',
  //     'background-position-y' : '0%'
  //   }, 500)
  // "

  $('.scripts').append(`
    <div data-script="${script}"
    style="--backdrop:url('assets/pictures/${script}.jpg')"
    
    onmousemove="pan(event,this)"
    >
      <h2>${scripts[script]["title"]}</h2>
      <p>${scripts[script]["description"]}</p>
      
      <span class="action-label">Explore Projects Made Using This Script</span>
      <div class="action-chips">
        <i data-icon="github"></i>
        <i data-icon="download"></i>
        <i data-icon="projects"></i>
        <i data-icon"raw ? top right clickable pseudo element ??"></i>
      </div>
      
      <a download href="https://raw.githubusercontent.com/D-Maxwell/NumworksScripts/main/${script}.py">
        <i style="background-image: url('assets/icons/download.png')"></i>
      </a>
    </div>
  `)
}



pan = (event, element) => {
  
  let elementRect = element.getClientRects()[0]
  elementPos = [elementRect.x, elementRect.y]
  elementDim = [elementRect.width, elementRect.height]
  
  let mousePos = [event.clientX, event.clientY]
  
  coverage = parseInt($(element).css('--_overflow')) / 100;
  
  $(element).css('--offset-x',
    ((mousePos[0] - elementPos[0]) / elementDim[0] * 2 - 1) * coverage / (coverage * 2 + 1) * 100 + "%"
  )
  $(element).css('--offset-y',
    ((mousePos[1] - elementPos[1]) / elementDim[1] * 2 - 1) * coverage / (coverage * 2 + 1) * 100 + "%"
  )
  
}

// <h5>${script}</h5>
