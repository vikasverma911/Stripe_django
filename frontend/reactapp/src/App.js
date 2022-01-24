import React, { useState, useEffect } from "react";
import { Route, Routes, BrowserRouter as Router } from "react-router-dom";
import HomePage from "./HomePage";
const App = () => (
    <Router>
        <Routes>
            <Route path='/' element={<HomePage/>} />
        </Routes>
    </Router>
);

export default App;