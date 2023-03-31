/** Context */
import {useContext, useEffect} from 'react'
import HardwareContext from '../../context/hardware/HardwareContext'
/** Component */
import HardwareItem from './HardwareItem';
import LoadingSpinner from '../layout/LoadingSpinner';
/** Icons */
import { Motherboard } from "react-bootstrap-icons";


export default function HardwareResults(  ) {
    /** Context */
    const { sensors, fetchSensors, loading } = useContext(HardwareContext)
    /** State */
    useEffect(() => {
        fetchSensors()
    }, []);
    /** Body */
    if (!loading) {
        return (
            <div className='card'>
                <div className="card-body text-start">
                    <h5 className="car-title"><Motherboard/> Sensors:</h5>
                </div>
                <ul className="list-group list-group-flush">
                    {sensors.map((sensor) => (
                        <HardwareItem
                            key={sensor.sensor_id}>
                                    {sensor.sensor_name}
                        </HardwareItem>
                    ))}
                </ul>
            </div>
        )
    } else {
        return <LoadingSpinner />
    }
}