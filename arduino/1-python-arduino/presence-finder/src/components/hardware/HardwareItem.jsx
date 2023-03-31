/** Icons */
import { Power } from "react-bootstrap-icons";

export default function HardwareItem( {children} ) {
    return (
        <li className="list-group-item text-end">
            <Power /> {children}
        </li>
    )
}