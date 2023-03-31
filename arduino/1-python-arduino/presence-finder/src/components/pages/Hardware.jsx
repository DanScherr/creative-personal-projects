/** Provider */
import { PresenceProvider } from "./../../context/hardware/HardwareContext";
/** Components */
import Navbar from "../layout/Navbar"
import HardwareResults from "../hardware/HardwareResults"


export default function Hardware(  ) {
    return (
        <PresenceProvider>
            <Navbar hardware='active'/>
            <div className="my-auto py-3">
                <HardwareResults />
            </div>
        </PresenceProvider>
    )
}