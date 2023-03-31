/** Provider */
import { ChartProvider } from "../../context/charts/ChartsContext"
/** Components */
import Navbar from "../layout/Navbar"
import ChartsResult from "../charts/ChartsResults"

export default function Charts(  ) {
    return (
        <ChartProvider>
            <Navbar charts='active'/>
            <div className="mx-auto py-3 text-center">
                <ChartsResult/>
            </div>
        </ChartProvider>
    )
}