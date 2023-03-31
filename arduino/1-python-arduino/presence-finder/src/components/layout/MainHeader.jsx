import ArduinoCommunityLogo_SVG from '../assets/ArduinoCommunityLogo_SVG.svg'

export default function MainHeader(  ) {
    return (
        <nav className="navbar bg-body-tertiary">
          <div className="container d-flex justify-content-center">
            <img src={ArduinoCommunityLogo_SVG} alt="Arduino community logo" width="400" height="250" />
          </div>
        </nav>
    )
}