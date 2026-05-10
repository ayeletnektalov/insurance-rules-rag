import express from "express";
import multer from "multer";
import path from "path";

const app = express();
const PORT = 3000;

// הגדרת שמירת קבצים
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads/");
  },

  filename: (req, file, cb) => {
    const uniqueName = Date.now() + path.extname(file.originalname);
    cb(null, uniqueName);
  },
});

const upload = multer({ storage });

// בדיקה שהשרת עובד
app.get("/", (req, res) => {
  res.send("Video Arrival Pipeline is running");
});

// endpoint להעלאת וידאו
app.post("/upload", upload.single("video_file"), (req, res) => {
  if (!req.file) {
    return res.status(400).json({
      error: "No file uploaded",
    });
  }

  res.json({
    message: "Video uploaded successfully",
    file: req.file.filename,
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});