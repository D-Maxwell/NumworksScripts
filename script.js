
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

      <a href="https://raw.githubusercontent.com/D-Maxwell/NumworksScripts/main/${script}.py" download>DOWNLOAD</a>
    </div>
  `)
}


// var previousMousePos = []
// var previousElement = ''

function pan(event,element){
  // if (element != previousElement) {
  //   previousMousePos = []
  //   previousElement = element
  // }

  let elementRect = element.getClientRects()[0]
  elementPos = [elementRect.x, elementRect.y]
  elementDim = [elementRect.width, elementRect.height]

  // console.log(previousElement, element);
  //
  // if (previousMousePos.length == 0) {
  //   previousMousePos = elementPos
  // }

  let mousePos = [event.clientX, event.clientY]


  // let movement = [
  //   mousePos[0] - previousMousePos[0],
  //   mousePos[1] - previousMousePos[1]
  // ]


  $(element).css('--background-position-x',
    (mousePos[0] - elementPos[0]) / elementDim[0] * (1/12) * 100 + "%"
    // parseInt($(element).css('--background-position-x')) + movement[0] + "px"
  )
  $(element).css('--background-position-y',
    (mousePos[1] - elementPos[1]) / elementDim[1] * (1/12) * 100 + "%"
    // parseInt($(element).css('--background-position-y')) + movement[1] + "px"
  )

  previousMousePos = mousePos
}

// <h5>${script}</h5>
