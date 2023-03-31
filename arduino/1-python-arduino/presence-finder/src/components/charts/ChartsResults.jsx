/** Context */
import {useContext, useEffect} from 'react'
import ChartsContext from '../../context/charts/ChartsContext'
/** Component */
import LoadingSpinner from '../layout/LoadingSpinner';
import ChartsItem from './ChartsItem';


export default function ChartsResult(  ) {
    /** Context */
    const { fetchPresences, presences, loading } = useContext(ChartsContext)
    /** State */
    useEffect(() => {
        fetchPresences()
    },[])

    let period = (
        presences.reduce((period, presence) => {
            return (period + parseInt(presence.detection))
        }, 0) / 60
    )

    /** Body */
    if (!loading) {
        return (
                <div>
                    <ChartsItem>
                        {period}      
                    </ChartsItem>
                </div>
            )
    } else {
        return <LoadingSpinner/>
    }
}