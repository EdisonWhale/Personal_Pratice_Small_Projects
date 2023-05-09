function openModal() {
    document.getElementById('task-modal').style.display = 'block';
  }
  
  document.getElementById('open-modal').addEventListener('click', function () {
    openModal();
  });
  
  document.getElementById('close-modal').addEventListener('click', function () {
    document.getElementById('task-modal').style.display = 'none';
  });
  
  document.getElementById('task-form').addEventListener('submit', function (event) {
    event.preventDefault();
    const taskTitle = document.getElementById('task-title').value;
    const taskDescription = document.getElementById('task-description').value;
    const taskCategory = document.getElementById('task-category').value;
    const taskPriority = document.getElementById('task-priority').value;
    const column = document.querySelector(`.box-column.${taskCategory}`);
    const task = createTaskElement(taskTitle, taskDescription, taskPriority);
    column.appendChild(task);
    document.getElementById('task-title').value = '';
    document.getElementById('task-description').value = '';
    updateTaskCount(taskCategory);
    document.getElementById('task-modal').style.display = 'none';
  });
  
  function createTaskElement(title, description, priority) {
    const task = document.createElement('div');
    task.classList.add('box');
    task.draggable = true;
    const today = new Date().toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
    task.innerHTML = `
      <div class="box-header">
        <span class="tag ${priority}" id="${priority}">${priority.charAt(0).toUpperCase() + priority.slice(1)}</span>
        <h4 class="title">${title}</h4>
        <button class="delete-button" aria-label="Delete task">
          <i class="fa-solid fa-trash-can"></i>
        </button>
      </div>
      <p class="description">${description}</p>
      <div class="box-footer">
        <div class="date">
          <i class="fa-solid fa-calendar"></i>
          <p>${today}</p>
        </div>
      </div>
    `;
    return task;
  }
  
  document.addEventListener('click', (event) => {
    const deleteButton = event.target.closest('.delete-button');
    if (deleteButton) {
      const task = deleteButton.closest('.box');
      task.remove();
    }
  });
  

  
  function updateTaskCount(category) {
    const column = document.querySelector(`.box-column.${category}`);
    const count = column.querySelectorAll('.box').length;
    const numElement = column.querySelector('.num');
    numElement.textContent = count;
  }
  
  const addTaskButtons = document.querySelectorAll('.add-task-button');
  
  addTaskButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const taskCategory = button.getAttribute('data-category');
      document.getElementById('task-category').value = taskCategory;
      openModal();
    });
  });
  