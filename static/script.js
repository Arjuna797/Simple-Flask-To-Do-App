async function addTask() {
  const task = document.getElementById('taskInput').value.trim();
  if (!task) return;
  const response = await fetch('/add', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ task })
  });
  location.reload();
}

async function markDone(task) {
  await fetch('/complete', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ task })
  });
  location.reload();
}

async function deleteTask(task) {
  await fetch('/delete', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ task })
  });
  location.reload();
}
