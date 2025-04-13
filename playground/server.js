const express = require("express");
const cors = require("cors");
const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(__dirname));

// Hardcoded test user (in a real application, this would be in a database)
const testUser = {
  username: "admin",
  password: "password123",
};

// Login endpoint
app.post("/login", (req, res) => {
  const { username, password } = req.body;

  if (username === testUser.username && password === testUser.password) {
    res.json({ success: true, message: "Login successful" });
  } else {
    res
      .status(401)
      .json({ success: false, message: "Invalid username or password" });
  }
});

// Start server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
