const mongoose = require("mongoose");

const connectDatabase = () => {
    mongoose.connect(process.env.DB_URL)
        .then((data) => {
            console.log(`MongoDB connected: ${data.connection.host}`);
        })
        .catch((err) => {
            console.error(`Connection failed: ${err.message}`);
            process.exit(1);
        });
};

module.exports = connectDatabase;