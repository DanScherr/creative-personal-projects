import spinner from './../assets/spinner.gif'

export default function LoadingSpinner(  ) {
    return (
        <div className='w-80 mt-20'>
            <img src={spinner} alt="Loading..." className="text-center" />
        </div>
    )
}