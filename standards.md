# Metro TV & Appliances - Coding & UI Standards
**Version 1.0 | For Desktop Applications Targeting Non-Tech-Savvy Users**

---

## 1. UI/UX Design Standards

### Typography
- **Primary Font**: Times New Roman for all text
- **Text Color**: Black (#000000) for all body text, headings, labels, and UI text
- **Font Sizes**:
  - Headings: 24pt minimum
  - Body text: 16pt minimum
  - Button text: 18pt minimum
  - Form labels: 16pt minimum
- **Line Height**: 1.6 minimum for better readability
- **Never use font sizes below 14pt**
- **Never use colored text for body copy** - black only for maximum readability

### Buttons
- **Minimum Size**: 60px height × 150px width
- **Recommended Size**: 80px height × 200px width for primary actions
- **Spacing**: Minimum 20px between buttons
- **Text**: Clear action words (e.g., "Save Ticket", "Search Customer")
- **States**:
  - Default: Clearly visible border and background
  - Hover: Subtle color change (maintain high contrast)
  - Disabled: Grayed out with reduced opacity (0.5)
- **Avoid**: Icon-only buttons, tiny "X" close buttons, split dropdowns

### Color & Contrast
- **Minimum Contrast Ratio**: 4.5:1 for normal text, 7:1 for optimal readability
- **Metro TV Color Palette**:
  - Background: Tan/Off-white (#F5F0E8) or lighter tan (#FAF7F2)
  - Primary text: Black (#000000) - use for all body text and headings
  - Primary buttons: Dark red (#B71C1C) with white text
  - Secondary buttons: White background with black text and dark red border
  - Success messages: Dark green (#2D5016) with light green background (#E8F5E9)
  - Error messages: Dark red (#B71C1C) with light red background (#FFEBEE)
  - Warning messages: Black (#000000) with light tan background (#FFF3E0)
  - Accents: Dark red (#B71C1C) for important UI elements
- **Black Usage**: Reserved primarily for text (body copy, headings, labels). Can be used for borders and dividers when necessary.
- **Avoid**: Low contrast grays, colored text for body copy, red/green for critical distinctions

### Layout & Spacing
- **Clickable Area**: Minimum 44px × 44px for all interactive elements
- **Margins**: 30px minimum around main content areas
- **Padding**: 20px minimum inside cards/containers
- **Form Fields**:
  - Height: 50px minimum
  - Width: Match content or full-width with max 600px
  - Spacing between fields: 25px minimum
- **Desktop Optimization**: Design for 1920×1080 and 1366×768 resolutions
- **Avoid**: Tiny icons, cramped layouts, horizontal scrolling

### Navigation
- **Menu Structure**: Simple, flat hierarchy (max 2 levels)
- **Menu Items**: Large, clearly labeled with 60px height minimum
- **Breadcrumbs**: Always show current location with 16pt text
- **Back Button**: Always visible and clearly labeled (not just an arrow)
- **Avoid**: Hamburger menus on desktop, hidden navigation, complex dropdowns

### Forms & Input
- **Labels**: Above input fields, never inside (placeholder text disappears)
- **Required Fields**: Mark clearly with "* Required" next to label
- **Input Validation**:
  - Show errors clearly with red text and icon
  - Explain what went wrong in plain English
  - Show errors near the problematic field
- **Submit Buttons**: Bottom right, large, clearly labeled
- **Avoid**: Inline validation before user finishes typing, cryptic error codes

### Feedback & Messaging
- **Success Messages**: Green banner at top, stays visible for 5 seconds
- **Error Messages**: Red banner at top, stays until dismissed
- **Loading States**: Show "Loading..." text with spinner, never just a spinner
- **Confirmations**: Use clear dialog boxes for destructive actions
  - Example: "Are you sure you want to delete this ticket? This cannot be undone."
- **Avoid**: Toast notifications (disappear too quickly), technical jargon, error codes without explanation

### Data Display
- **Tables**:
  - Row height: 60px minimum
  - Alternate row colors for readability
  - Column headers: Bold, 18pt
  - Sortable columns: Clear up/down arrows
- **Search Results**: Show count (e.g., "Found 23 tickets")
- **Empty States**: Show helpful message (e.g., "No tickets found. Try different search terms.")
- **Avoid**: Tiny checkboxes, pagination without page numbers, infinite scroll

---

## 2. Python Coding Standards

### File Organization
```python
# 1. Standard library imports
import os
import json
from datetime import datetime

# 2. Third-party imports
import requests
from flask import Flask, request

# 3. Local application imports
from utils.database import connect_db
from config import API_KEY
```

### Naming Conventions
- **Functions**: `snake_case` - `def get_service_ticket():`
- **Variables**: `snake_case` - `ticket_number = "12345"`
- **Constants**: `UPPER_SNAKE_CASE` - `API_ENDPOINT = "https://api.example.com"`
- **Classes**: `PascalCase` - `class ServiceTicket:`
- **Private methods**: Prefix with underscore - `def _validate_response():`

### Comments & Documentation
```python
def create_lotus_ticket(servicepower_data):
    """
    Creates a ticket in Lotus system from ServicePower data.
    
    Args:
        servicepower_data (dict): Dictionary containing ticket info from ServicePower
        
    Returns:
        str: Lotus ticket ID if successful, None if failed
        
    Example:
        ticket_id = create_lotus_ticket({"customer": "John Doe", "issue": "Fridge not cooling"})
    """
    # Extract customer name from ServicePower response
    customer_name = servicepower_data.get('customer_name')
    
    # Validate required fields before creating ticket
    if not customer_name:
        print("ERROR: Missing customer name")
        return None
```

### Error Handling
```python
# GOOD: Specific error handling with user-friendly messages
try:
    response = requests.post(API_ENDPOINT, json=ticket_data, timeout=30)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("ERROR: ServicePower API timed out after 30 seconds. Please try again.")
    return None
except requests.exceptions.RequestException as e:
    print(f"ERROR: Could not connect to ServicePower API. Details: {e}")
    return None

# BAD: Generic error handling
try:
    response = requests.post(API_ENDPOINT, json=ticket_data)
except Exception as e:
    print(f"Error: {e}")
```

### Code Structure
- **Max function length**: 50 lines (break into smaller functions if longer)
- **Max line length**: 100 characters
- **Indentation**: 4 spaces (never tabs)
- **Blank lines**: 2 between functions, 1 within functions for logical sections

### Configuration & Secrets
```python
# GOOD: Use environment variables or config files
import os
API_KEY = os.getenv('SERVICEPOWER_API_KEY')
API_ENDPOINT = os.getenv('SERVICEPOWER_ENDPOINT', 'https://default-url.com')

# BAD: Hardcoded credentials
API_KEY = "sk_live_12345abcdef"  # NEVER DO THIS
```

### Logging
```python
import logging

# Set up logging at the start of your script
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

# Use throughout your code
logging.info("Starting ticket sync process")
logging.warning("No tickets found for today")
logging.error(f"Failed to create ticket: {error_message}")
```

---

## 3. Node.js/JavaScript Coding Standards

### File Organization
```javascript
// 1. External dependencies
const express = require('express');
const axios = require('axios');

// 2. Internal modules
const dbUtils = require('./utils/database');
const config = require('./config');

// 3. Constants
const API_TIMEOUT = 30000;
```

### Naming Conventions
- **Functions**: `camelCase` - `function getServiceTicket() {}`
- **Variables**: `camelCase` - `const ticketNumber = "12345"`
- **Constants**: `UPPER_SNAKE_CASE` - `const API_ENDPOINT = "https://api.example.com"`
- **Classes**: `PascalCase` - `class ServiceTicket {}`
- **File names**: `kebab-case` - `service-ticket-handler.js`

### Modern JavaScript
```javascript
// GOOD: Use const/let, never var
const apiKey = process.env.API_KEY;
let ticketCount = 0;

// GOOD: Use arrow functions for callbacks
const tickets = data.map(item => item.ticketId);

// GOOD: Use async/await for promises
async function fetchTickets() {
    try {
        const response = await axios.get(API_ENDPOINT);
        return response.data;
    } catch (error) {
        console.error('Failed to fetch tickets:', error.message);
        return null;
    }
}

// GOOD: Use template literals
const message = `Found ${ticketCount} tickets for customer ${customerName}`;
```

### Error Handling
```javascript
// GOOD: Specific error handling
async function createTicket(ticketData) {
    try {
        const response = await axios.post(API_ENDPOINT, ticketData, {
            timeout: 30000
        });
        return response.data;
    } catch (error) {
        if (error.code === 'ECONNABORTED') {
            console.error('Request timed out after 30 seconds');
        } else if (error.response) {
            console.error(`API error: ${error.response.status} - ${error.response.data.message}`);
        } else {
            console.error('Network error:', error.message);
        }
        return null;
    }
}
```

---

## 4. Tailwind CSS Standards

### Desktop-First Approach
```html
<!-- GOOD: Base styles for desktop, adjust for smaller if needed -->
<button class="h-20 w-52 text-lg bg-red-800 text-white hover:bg-red-700">
    Save Ticket
</button>

<!-- Main content area with proper spacing and tan background -->
<div class="max-w-7xl mx-auto px-8 py-8 bg-[#F5F0E8]">
    <h1 class="text-3xl mb-6 text-black" style="font-family: 'Times New Roman', serif;">
        Service Tickets
    </h1>
</div>
```

### Component Patterns
```html
<!-- Large, accessible buttons with Metro TV colors -->
<button class="
    h-20 min-w-[200px] px-8
    text-lg font-normal
    bg-red-800 text-white
    hover:bg-red-700
    rounded-lg
    disabled:opacity-50 disabled:cursor-not-allowed
">
    Primary Action
</button>

<!-- Secondary button style -->
<button class="
    h-20 min-w-[200px] px-8
    text-lg font-normal
    bg-white text-black border-2 border-red-800
    hover:bg-[#FAF7F2]
    rounded-lg
    disabled:opacity-50 disabled:cursor-not-allowed
">
    Secondary Action
</button>

<!-- Form inputs on tan background -->
<div class="mb-6">
    <label class="block text-base mb-2 font-semibold text-black">
        Customer Name <span class="text-red-700">* Required</span>
    </label>
    <input 
        type="text"
        class="h-12 w-full max-w-2xl px-4 text-base text-black bg-white border-2 border-gray-400 rounded focus:border-red-700 focus:outline-none"
    />
</div>

<!-- Data table with tan striping -->
<table class="w-full border-collapse bg-white">
    <thead>
        <tr class="bg-[#F5F0E8]">
            <th class="text-left p-4 text-lg font-bold border-b-2 border-black text-black">Ticket #</th>
            <th class="text-left p-4 text-lg font-bold border-b-2 border-black text-black">Customer</th>
            <th class="text-left p-4 text-lg font-bold border-b-2 border-black text-black">Status</th>
        </tr>
    </thead>
    <tbody>
        <tr class="even:bg-[#FAF7F2] h-16 hover:bg-[#F5F0E8]">
            <td class="p-4 text-base text-black">12345</td>
            <td class="p-4 text-base text-black">John Doe</td>
            <td class="p-4 text-base text-black">
                <span class="px-4 py-2 bg-green-100 text-green-800 rounded">Complete</span>
            </td>
        </tr>
    </tbody>
</table>
```

### Typography
```html
<!-- Always specify Times New Roman and black text -->
<style>
    body {
        font-family: 'Times New Roman', serif;
        color: #000000;
        background-color: #F5F0E8;
    }
</style>

<!-- Or inline for specific elements -->
<h1 style="font-family: 'Times New Roman', serif; color: #000000;" class="text-3xl">
    Page Title
</h1>

<p class="text-base text-black">
    All body text should be black for maximum readability.
</p>
```

### Color Palette
```javascript
// tailwind.config.js
module.exports = {
    theme: {
        extend: {
            colors: {
                'metro-red': '#B71C1C',
                'metro-red-dark': '#8B0000',
                'metro-tan': '#F5F0E8',
                'metro-tan-light': '#FAF7F2',
                'metro-success': '#2D5016',
                'metro-error': '#B71C1C',
                'metro-warning': '#000000',
            },
            backgroundColor: {
                'metro-base': '#F5F0E8',
            }
        }
    }
}
```

---

## 5. Firebase Standards (Future Use)

### Security Rules
```javascript
// Firestore Security Rules - Start restrictive, open up as needed
rules_version = '2';
service cloud.firestore {
    match /databases/{database}/documents {
        // Only authenticated users can read/write their own data
        match /tickets/{ticketId} {
            allow read, write: if request.auth != null 
                && request.auth.uid == resource.data.technicianId;
        }
    }
}
```

### Data Structure
```javascript
// GOOD: Flat, denormalized structure for reads
const ticketData = {
    ticketId: "12345",
    customerName: "John Doe",
    customerPhone: "555-1234",
    serviceType: "Refrigerator Repair",
    status: "Open",
    assignedTech: "Aaron",
    createdAt: serverTimestamp(),
    updatedAt: serverTimestamp()
};

// BAD: Deeply nested structure
const ticketData = {
    customer: {
        personal: {
            name: { first: "John", last: "Doe" },
            contact: { phone: "555-1234" }
        }
    }
};
```

### Error Handling
```javascript
// Firebase operations with proper error handling
async function saveTicket(ticketData) {
    try {
        const docRef = await db.collection('tickets').add(ticketData);
        console.log('Ticket saved with ID:', docRef.id);
        return docRef.id;
    } catch (error) {
        console.error('Failed to save ticket:', error.message);
        alert('Could not save ticket. Please check your internet connection and try again.');
        return null;
    }
}
```

---

## 6. General Best Practices

### Version Control (Git)
```bash
# Commit messages should be clear and descriptive
git commit -m "Add customer phone validation to service ticket form"

# Not just:
git commit -m "updates"
```

### Testing
- Test on both 1920×1080 and 1366×768 resolutions
- Test with actual target users (non-tech-savvy staff)
- Test all error scenarios (network failures, timeouts, invalid data)

### Documentation
- README file in every project explaining:
  - What the project does
  - How to install/run it
  - Required environment variables
  - Common troubleshooting steps

### Performance
- Set reasonable timeouts (30 seconds for API calls)
- Show loading indicators for operations over 1 second
- Cache frequently accessed data
- Optimize images (compress before uploading)

---

## Quick Reference Checklist

**Before starting any project, verify:**
- [ ] All fonts set to Times New Roman
- [ ] All text in black (#000000)
- [ ] Backgrounds in tan/off-white (#F5F0E8 or #FAF7F2)
- [ ] Primary buttons: Dark red (#B71C1C) with white text
- [ ] Minimum button size: 60px × 150px
- [ ] Minimum text size: 16pt
- [ ] High contrast colors (4.5:1 minimum ratio)
- [ ] Error messages in plain English
- [ ] Loading states for all async operations
- [ ] Mobile responsiveness disabled (desktop-only)
- [ ] All interactive elements at least 44px × 44px
- [ ] Form labels above inputs (not placeholders)
- [ ] Clear success/error feedback for all actions

**Code Quality:**
- [ ] No hardcoded credentials
- [ ] Proper error handling with user-friendly messages
- [ ] Logging for debugging
- [ ] Comments explaining WHY, not just WHAT
- [ ] Functions under 50 lines
- [ ] Consistent naming conventions

---

*Last updated: December 2024*