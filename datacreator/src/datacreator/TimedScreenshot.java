package datacreator;

public class TimedScreenshot extends Screenshot {

	private int timed_id;

	public TimedScreenshot() {
	}

	public TimedScreenshot(int timed_id, String content, String type, String classname, String title, String comment, String start) {
		super(content, type, classname, title, comment, start);
		this.timed_id = timed_id;
	}

	public int getTimed_id() {
		return timed_id;
	}

	public void setTimed_id(int timed_id) {
		this.timed_id = timed_id;
	}

}
