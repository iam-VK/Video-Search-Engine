import './MainPage.css'
import Header from "../../components/header/Header"
import Body from "../../components/body/Body"

function MainPage()
{
    return (
        <div>
            <div className="appcontent">
                <Header subtitle={"Find your videos"} />
                <Body path={"search/"} />
            </div>
        </div>
    )
}

export default MainPage
