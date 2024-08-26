const mentorsData = {
    'PAT': ['Chandra sir', 'Tushar sir', 'Amir sir'],
    'JAT': ['Chandra sir'],
    'PD': ['Chandra sir']
};

const mentorTimeSlots = {
    'Chandra sir': ['12pm-1pm', '1pm-2pm', '2pm-3pm', '3pm-4pm', '4pm-5pm', '5pm-6pm', '6pm-7pm'],
    'Tushar sir': ['11am-12pm', '12pm-1pm', '1pm-2pm'],
    'Amir sir': ['3pm-4pm', '4pm-5pm', '5pm-6pm']
};

function updateMentors() {
    const technology = document.getElementById('technology').value;
    const mentorSelect = document.getElementById('mentor');
    mentorSelect.innerHTML = '';  // Clear previous options

    mentorsData[technology].forEach(mentor => {
        const option = document.createElement('option');
        option.value = mentor;
        option.textContent = mentor;
        mentorSelect.appendChild(option);
    });

    updateTimeSlots();  // Update time slots based on the selected mentor
}

function updateTimeSlots() {
    const mentor = document.getElementById('mentor').value;
    const timeSelect = document.getElementById('time');
    timeSelect.innerHTML = '';  // Clear previous options

    mentorTimeSlots[mentor].forEach(timeSlot => {
        const option = document.createElement('option');
        option.value = timeSlot;
        option.textContent = timeSlot;
        timeSelect.appendChild(option);
    });
}

// Initialize form with default mentor and time slots
document.addEventListener('DOMContentLoaded', function () {
    updateMentors();
});
