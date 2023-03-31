/** Router */
import { Link } from 'react-router-dom'
/** Icons */
import { BarChartLineFill, Motherboard, HouseFill } from "react-bootstrap-icons";
/** Props */
import { PropTypes } from 'prop-types'


export default function Navbar( {home, charts, hardware} ) {
    return (
        <nav className="navbar navbar-expand-lg bg-body-secondary">
            <div className="container-fluid">

                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>

                <div className="collapse navbar-collapse " id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="navbar-item d-flex justify-content-center">
                            <Link to='/' className={`nav-link ${home}`}><HouseFill /> Home</Link>
                        </li>
                        <li className="navbar-item d-flex justify-content-center">
                            <Link to="/charts" className={`nav-link ${charts}`} aria-current=""><BarChartLineFill/> Charts</Link>
                        </li>
                        <li className="navbar-item d-flex justify-content-center">
                            <Link to="/hardware" className={`nav-link ${hardware}`} aria-current=""><Motherboard /> Hardware</Link>
                        </li>
                    </ul>
                </div>

            </div>
        </nav>
    )
}

Navbar.defaultProps = {
    home: '',
    charts: '',
    hardware: '',
}

Navbar.propTypes = {
    title: PropTypes.string,
}