package images;

public class testImages {

	public static void main(String[] args)
	{
		JerseyGetImageData test = new JerseyGetImageData("http://192.168.142.128/api/");
		imageDataQuery testQuery = new imageDataQuery();
		testQuery.addDescription("Yay Pretty Picture!");
		testQuery.addAltText("Holla Holla Get Dolla.");
		//test.addImage("C:/Users/Dan/Desktop/Art Folders/Fantasty/Magic 1600 x 1200.jpg", testQuery);
		//test.getImageInfo(12);
		//testQuery.addDescription("Huzzah!");
		//test.editImageInfo(13, testQuery);
		test.deleteImage(13);
	}
}