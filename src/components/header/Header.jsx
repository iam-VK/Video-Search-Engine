import "./header.css"
function Header({ subtitle })
{
    return (
        <>
            <header className="header">
                <h1>Video Search Engine</h1>
            </header>
            <div className="container">
                <div className="typed-out">
                    {subtitle}
                </div>
            </div>
        </>
    )
}


export default Header