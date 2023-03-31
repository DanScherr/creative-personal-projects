/** Routes */
import { BrowserRouter as Router, Route, Routes } from "react-router-dom"
/** Pages */
import Home from "./components/pages/Home";
import Charts from "./components/pages/Charts";
import Hardware from "./components/pages/Hardware";
/** Layouts */
import MainHeader from "./components/layout/MainHeader";
import MainFooter from "./components/layout/MainFooter";
/** utilities */


function App() {
  return (
    <div className="bg-dark-subtle" style={{height: '100vh'}}>
      <div className="container">
        <Router>
          <header>
            <MainHeader />
          </header>

          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/charts" element={<Charts />} />
            <Route path="/hardware" element={<Hardware />} />
          </Routes>

          <footer>
            <MainFooter />
          </footer>
        </Router>
      </div>
    </div>
  );
}

export default App;
