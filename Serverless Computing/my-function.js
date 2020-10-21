exports.handler = async (event) => 
{
    // TODO implement
    var dt = new Date();
    const response = 
    {
        statusCode: 200,
        body: "Hello from Lambda! \n\nGreenwich Mean Time is " + dt,

    };
    return response;
};
