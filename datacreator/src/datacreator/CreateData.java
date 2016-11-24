package datacreator;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.time.Clock;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class CreateData {

	public static void main(String[] args) {
		CreateData cd = new CreateData();
		cd.createManualScreenshotImages();
		cd.createClickScreenshotImages();
		cd.createTimedScreenshotImages();
		cd.createKeyPress();
	}
	
	
	private void createKeyPress(){
		LocalDateTime today = LocalDateTime.now(Clock.systemUTC());
		LocalDateTime twoWeeksAgo = today.minus(2, ChronoUnit.WEEKS);
		
		List<KeyPress> keyPresses = new ArrayList<>();
		int count = 0;
		String start;
		while(twoWeeksAgo.isBefore(today)) {
			twoWeeksAgo = twoWeeksAgo.plus(45, ChronoUnit.MINUTES);
			start = twoWeeksAgo.truncatedTo(ChronoUnit.SECONDS).format(DateTimeFormatter.ISO_LOCAL_DATE_TIME);
			keyPresses.add(new KeyPress(count, "some key presses", "Keypresses", start));
			count++;
		}

		print("keypressData.json", keyPresses);
	}
	
	private void createManualScreenshotImages(){
		LocalDateTime today = LocalDateTime.now(Clock.systemUTC());
		LocalDateTime twoWeeksAgo = today.minus(2, ChronoUnit.WEEKS);
		
		List<ManualScreenshot> screeenshots = new ArrayList<>();
		int count = 0;
		String start;
		while(twoWeeksAgo.isBefore(today)) {
			twoWeeksAgo = twoWeeksAgo.plus(45, ChronoUnit.MINUTES);
			start = twoWeeksAgo.truncatedTo(ChronoUnit.SECONDS).format(DateTimeFormatter.ISO_LOCAL_DATE_TIME);
			screeenshots.add(new ManualScreenshot(count, " ", "point", "imgPoint", "", "C:\\temp\\json\\images\\manualscreenshot\\someimagename.png", start));
			count++;
		}

		print("snap.json", screeenshots);
	}
	
	private void createClickScreenshotImages(){
		LocalDateTime today = LocalDateTime.now(Clock.systemUTC());
		LocalDateTime twoWeeksAgo = today.minus(2, ChronoUnit.WEEKS);
		
		List<ClickScreenshot> screeenshots = new ArrayList<>();
		int count = 0;
		String start;
		while(twoWeeksAgo.isBefore(today)) {
			twoWeeksAgo = twoWeeksAgo.plus(45, ChronoUnit.MINUTES);
			start = twoWeeksAgo.truncatedTo(ChronoUnit.SECONDS).format(DateTimeFormatter.ISO_LOCAL_DATE_TIME);
			screeenshots.add(new ClickScreenshot(count, " ", "point", "imgPoint", "", "C:\\temp\\json\\images\\click\\someimagename.png", start));
			count++;
		}

		print("click.json", screeenshots);
	}
	
	private void createTimedScreenshotImages(){
		LocalDateTime today = LocalDateTime.now(Clock.systemUTC());
		LocalDateTime twoWeeksAgo = today.minus(2, ChronoUnit.WEEKS);
		
		List<TimedScreenshot> screeenshots = new ArrayList<>();
		int count = 0;
		String start;
		while(twoWeeksAgo.isBefore(today)) {
			twoWeeksAgo = twoWeeksAgo.plus(45, ChronoUnit.MINUTES);
			start = twoWeeksAgo.truncatedTo(ChronoUnit.SECONDS).format(DateTimeFormatter.ISO_LOCAL_DATE_TIME);
			screeenshots.add(new TimedScreenshot(count, " ", "point", "imgPoint", "", "C:\\temp\\json\\images\\timed\\someimagename.png", start));
			count++;
		}

		print("timed.json", screeenshots);
	}

	private void print(String fileName, List<?> theList){
		try (Writer writer = new FileWriter(fileName)) {
		    Gson gson = new GsonBuilder().setPrettyPrinting().create();
		    gson.toJson(theList, writer);
		} catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println(fileName + " Done");

	}
}

