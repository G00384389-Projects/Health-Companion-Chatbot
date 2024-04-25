
function Home() {

    return (
        <div>
            <div className="container px-4 px-lg-5">
                {/* Image and Description Section */}
                <div className="row gx-4 gx-lg-5 align-items-center my-5">
                    {/* Image */}
                    <div className="col-lg-7"><img className="img-fluid rounded mb-4 mb-lg-0" src="https://media.istockphoto.com/id/935941772/photo/diverse-people-holding-emoticon.jpg?s=612x612&w=0&k=20&c=EHtZW3x-u7sS0Tg9WZdvLz_LCMrDqx0Xu6xw_fI6qEM=" alt="..." /></div>

                    {/* Text */}
                    <div className="col-lg-5">
                        <h1 className="font-weight-light">AI Wellness Companion</h1>
                        <p>
                        We believe that taking care of your health is a multifaceted journey that involves a balanced approach to body, mind, and spirit. 
                        Here are some foundational steps you can take to nurture all aspects of your well-being:
                        </p>
                        <p></p>
                        
                    </div>
                </div>

                {/* Additional Info Section */}
                <div className="card text-white bg-secondary my-5 py-4 text-center">
                    <div className="card-body"><h3 className="text-white m-0">See the features of our website below!</h3></div>
                </div>

                {/* Cards Section */}
                <div className="row gx-4 gx-lg-5">
                    {/* Product Info Card */}
                    <div className="col-md-4 mb-5">
                        <div className="card h-100">
                            <div className="card-body">
                                <h2 className="card-title">Talk to our AI Companion</h2>
                                <p className="card-text">See our store.</p>
                            </div>
                            <div className="card-footer"><a className="btn btn-primary btn-sm" href="/chatBot">Browse</a></div>
                        </div>
                    </div>
                    {/* About Us Card */}
                    <div className="col-md-4 mb-5">
                        <div className="card h-100">
                            <div className="card-body">
                                <h2 className="card-title">About Us</h2>
                                <p className="card-text">To learn more about us!</p>
                            </div>
                            <div className="card-footer"><a className="btn btn-primary btn-sm" href="/aboutUS">Click here</a></div>
                        </div>
                    </div>
                    {/* Login Card */}
                    <div className="col-md-4 mb-5">
                        <div className="card h-100">
                            <div className="card-body">
                                <h2 className="card-title">Mood Checker</h2>
                                <p className="card-text">Log your mood every day</p>
                            </div>
                            <div className="card-footer"><a className="btn btn-primary btn-sm" href="/moodChecker">Click here </a></div>
                        </div>
                    </div>
                    {/* API Card - Full Width */}
                    <div className="col-md-12 mb-5">
                        <div className="card h-100">
                            <div >
                                <div className="card-body">
                                    <h2 className="card-title">Daily News</h2>
                                    <p className="card-text"></p>
                                </div>
                                <div className="card-footer"><a className="btn btn-primary btn-sm" href="/newsList">Click here</a></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div style={{ margin: '200px' }}></div>
        </div>
    );
}

export default Home;