document.addEventListener('DOMContentLoaded', function () {
    // Function to add a new element
    function addElement() {
    
      var input = document.getElementById('add-to-list-input');

      const elementsContainer = document.querySelector('.elements-container');
      const newElement = document.createElement('div');
      newElement.classList.add("wrapper");
      newElement.innerHTML = `
      <div class="left-element element">
        <p>${input.value}</p>
        </div>
        <div class="right-element">
            <button class="remove-element">Remove</button>
        </div>
      `;
      elementsContainer.appendChild(newElement);
  
      // Clear the input
      input.value = '';
  
      // Add remove functionality to the new button
      newElement.querySelector('.remove-element').addEventListener('click', function() {
        elementsContainer.removeChild(newElement);
      });
    counter += 1;
    }
  
    // Attach event to the "Add to List" button
    var counter = 0;
    document.querySelector('.add-to-list-btn').addEventListener('click', addElement);
    

    // Attach the remove functionality to existing remove buttons
    document.querySelectorAll('.remove-element').forEach(button => {
      button.addEventListener('click', function() {
        const elementDiv = button.closest('.wrapper');
        elementDiv.parentNode.removeChild(elementDiv);
      });
    });
  });



document.addEventListener('DOMContentLoaded', function () {
    // Event listener for the 'Create List' button
    document.getElementById('create-list').addEventListener('click', function() {
      // Get the list name
      const listName = document.getElementById('list-name').value;
        
      // Get all element inputs
      const elements_nodes = document.querySelectorAll('.elements-container .wrapper .element');
      
      let elements = []; // Array to hold the dictionaries
        
      elements_nodes.forEach(elementDiv => {
        console.log(elementDiv);
        const pTag = elementDiv.querySelector('p');
        
        const text = pTag.textContent; // Getting the text
        console.log(text);
        elements.push({ name: text }); // Adding the dictionary to the array
        
        });

        console.log(elements); // Log the array to see the result
   
      
  
      // Prepare the data to be sent
      const dataToSend = {
        list: {
          name: listName,
          city: "Hamburg", 
          author: 2 
        },
        elements: elements
      };
  
      // Send the POST request
      fetch('http://localhost:8000/lists/create_list_with_element', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          // Add other headers like authentication tokens if needed
        },
        body: JSON.stringify(dataToSend)
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
      })
      .then(data => {
        console.log('Success:', data);
        // Handle success, like redirecting to a new page or showing a success message
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle errors, like showing an error message to the user
      });
    });
  });


